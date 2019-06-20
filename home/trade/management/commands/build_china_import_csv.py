import csv
import json

from django.conf import settings
from django.core.management.base import BaseCommand

from trade.models import ChinaImport, ChinaImportComment, ChinaImportThumbs


pretty_name = {
    'score': 'Score',
    'shipmentmonth': 'Month Shipped',
    'consigneename': 'Consignee Name',
    'consigneecity': 'Consignee City',
    'consigneepanjivaid': 'Consignee',
    'consigneecountry': 'Consignee Country',
    'shipmentorigin': 'Shipment Origin',
    'province': 'Province',
    'countryofsale': 'Country of Sale',
    'transportmethod': 'Transport Method',
    'iscontainerized': 'Containerized',
    'valueofgoodsusd': 'Value',
    'hscode': 'HS Code',
    'hscodekeywords': 'HS Code Keywords',
    'adminregion': 'Admin Region',
    'tradetype': 'Trade Type',
    'panjivarecordid': 'panjivarecordid'
}


def custom_format(instance, field):
    value = getattr(instance, field, '')
    if field in ['valueofgoodsusd']:
        return '${:,}'.format(value)
    if field in ['shipmentmonth']:
        return value.strftime('%Y/%m')
    return value


class Command(BaseCommand):
    help = 'Builds the csv for the output file'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **options):
        with open(options['path']) as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            output = process_score_rows(reader)

            outfilepath = settings.ROOT_DIR + 'home' + settings.STATIC_ROOT + 'china_import.json'
            with open(outfilepath, 'w') as outfile:
                json.dump(output, outfile)

            self.stdout.write(self.style.SUCCESS('Successfully wrote to file "%s"' % outfilepath))


def process_score_rows(iterable):
    scores = {}
    for row in iterable:
        scores[row[0]] = row
    return process_scores(scores)


def process_scores(scores):
    print(scores)
    ids = list(scores.keys())[:10000]
    print("Came up with {} ids".format(len(scores.keys())))

    model_cls = ChinaImport
    comment_cls = ChinaImportComment
    thumbs_cls = ChinaImportThumbs
    show_fields = ['shipmentmonth', 'consigneecountry', 'consigneepanjivaid', 'shipmentorigin', 'countryofsale', 'hscode', 'valueofgoodsusd']
    hidden_fields = ['consigneename', 'consigneecity', 'province', 'transportmethod', 'iscontainerized', 'adminregion', 'tradetype', 'hscodekeywords', 'panjivarecordid']

    # scores = {pajiva_id: 1.0 for pajiva_id in ids}

    print("Got ids")

    # comment_data = {}
    # for panjivarecordid in ids:
    #     comments = comment_cls.objects.filter(panjivarecordid=panjivarecordid)
    #     if comments.exists():
    #         comment_data[panjivarecordid] = comments[0].comment
    # print("Massaged comments")

    # thumbs_data = {}
    # for panjivarecordid in ids:
    #     thumbs = thumbs_cls.objects.filter(panjivarecordid=panjivarecordid)
    #     if thumbs.exists():
    #         thumbs_data[panjivarecordid] = thumbs[0].thumbs
    # print("Massaged comments")

    comments = comment_cls.objects.filter(panjivarecordid__in=ids)
    comment_data = {comment.panjivarecordid: comment.comment for comment in comments}
    print("Massaged comments")

    thumbs = thumbs_cls.objects.filter(panjivarecordid__in=ids)
    thumbs_data = {thumb.panjivarecordid: thumb.thumbs for thumb in thumbs}
    print("Massaged thumbs")

    data = []
    for instance in model_cls.objects.using('wwf').filter(panjivarecordid__in=ids):
        data.append([
            '{:.3f}'.format(float(scores[str(instance.panjivarecordid)][1])),
        ] + [
            custom_format(instance, field) for field in show_fields
        ] + [
            custom_format(instance, field) for field in hidden_fields
        ] + [
            comment_data[instance.panjivarecordid] if instance.panjivarecordid in comment_data else ''
        ] + [
            'thumbs-' + thumbs_data[instance.panjivarecordid] if instance.panjivarecordid in thumbs_data else ''
        ])

    print("Computed data")
    print(data)

    fields = ['score'] + show_fields + hidden_fields + ['comment', 'thumbs']
    id_index = len(fields) - 3  # the most magic of numbers

    columns = [{
        'className': "details-control",
        'orderable': False,
        'data': None,
        'defaultContent': ""
    }] + [{
        'title': pretty_name[field] if field in pretty_name else field,
        'data': i
    } for i, field in enumerate(fields)]

    output = {
        'columns': columns,
        'id_index': id_index,
        'hidden_cols': list(range(len(show_fields) + 2, len(fields) + 1)),
        'data': data,
    }

    return output
