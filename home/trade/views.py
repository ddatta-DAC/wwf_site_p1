import json

from django.apps import apps
from django.conf import settings
from django.http import JsonResponse, HttpResponseNotAllowed, Http404
from django.views import View
from django.views.generic.detail import DetailView, BaseDetailView

from .management.commands.parsers import ChinaImportParser, ChinaExportParser, PeruExportParser, UsImportParser
from .models import ChinaExport, PeruExport, UsImport, ChinaImport, Flags
from .tasks import rebuild_csv
from feedback.models import (
    ChinaExportComment,
    ChinaImportComment,
    PeruExportComment,
    UsImportComment,
    ChinaExportThumbs,
    ChinaImportThumbs,
    PeruExportThumbs,
    UsImportThumbs
)


def format(instance, field):
    value = getattr(instance, field, '')
    if field in ['valueofgoodsusd']:
        return '${:,}'.format(value)
    if field in ['shipmentmonth']:
        return value.strftime('%Y/%m')
    return value


class DefaultExpandRowView(DetailView):
    def get(self, request):
        raise Http404


class AnomalyApiView(BaseDetailView):
    template_name = 'anomaly.html'
    slug_field = 'panjivarecordid'
    slug_url_kwarg = 'panjivarecordid'

    def get_queryset(self):
        trade_config = apps.get_app_config('trade')

        if self.kwargs['track_name'] == 'china_import':
            self.parser_cls = ChinaImportParser
            self.scores = trade_config.get_china_import()
            self.list_i = 4
            return ChinaImport.objects.using('wwf').all()
        elif self.kwargs['track_name'] == 'china_export':
            self.parser_cls = ChinaExportParser
            self.scores = trade_config.get_china_export()
            self.list_i = 3
            return ChinaExport.objects.using('wwf').all()
        elif self.kwargs['track_name'] == 'peru_export':
            self.parser_cls = PeruExportParser
            self.scores = trade_config.get_peru_export()
            self.list_i = 4
            return PeruExport.objects.using('wwf').all()
        elif self.kwargs['track_name'] == 'us_import':
            self.parser_cls = UsImportParser
            self.scores = trade_config.get_us_import()
            self.list_i = 3
            return UsImport.objects.using('wwf').all()
        return None

    def render_to_response(self, context, *args, **kwargs):
        record = None
        for row in self.scores:
            if row[0] == self.kwargs['panjivarecordid']:
                record = row
                break

        if record is None:
            return JsonResponse({
                'status': '404'
            })

        parser = self.parser_cls([[pid, 0] for pid in record[self.list_i].split(';')])
        output = parser.process_scores(skip_scores=True)
        return JsonResponse(output)


class AnomalyView(DetailView):
    template_name = 'anomaly.html'
    slug_field = 'panjivarecordid'
    slug_url_kwarg = 'panjivarecordid'

    def get_queryset(self):
        if self.kwargs['track_name'] == 'china_import':
            self.parser_cls = ChinaImportParser
            return ChinaImport.objects.using('wwf').all()
        elif self.kwargs['track_name'] == 'china_export':
            self.parser_cls = ChinaExportParser
            return ChinaExport.objects.using('wwf').all()
        elif self.kwargs['track_name'] == 'peru_export':
            self.parser_cls = PeruExportParser
            return PeruExport.objects.using('wwf').all()
        elif self.kwargs['track_name'] == 'us_import':
            self.parser_cls = UsImportParser
            return UsImport.objects.using('wwf').all()
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        fake_iterable = [[self.kwargs['panjivarecordid'], 0]]
        parser = self.parser_cls(fake_iterable)
        output = parser.process_scores(skip_scores=True)
        anomaly_data = json.dumps(output)

        if self.kwargs['track_name'] == 'china_import':
            context['track_type_name'] = 'China Import'
        elif self.kwargs['track_name'] == 'china_export':
            context['track_type_name'] = 'China Export'
        elif self.kwargs['track_name'] == 'peru_export':
            context['track_type_name'] = 'Peru Export'
        elif self.kwargs['track_name'] == 'us_import':
            context['track_type_name'] = 'US Import'

        context['track_name'] = self.kwargs['track_name']
        context['anomaly'] = anomaly_data
        return context


class BaseExpandedRowView(DetailView):
    template_name = 'partials/_expanded_row.html'
    slug_field = 'panjivarecordid'
    slug_url_kwarg = 'panjivarecordid'

    def get_queryset(self):
        return self.transaction_cls.objects.using('wwf').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comment = ''
        try:
            comment_obj = self.comment_cls.objects.get(
                panjivarecordid=self.object.panjivarecordid,
                user=self.request.user
            )
            comment = comment_obj.comment
        except self.comment_cls.DoesNotExist:
            pass
        all_comments = self.comment_cls.objects.filter(panjivarecordid=self.object.panjivarecordid)

        thumbs = 'clear'
        try:
            thumbs_obj = self.thumbs_cls.objects.get(
                panjivarecordid=self.object.panjivarecordid,
                user=self.request.user
            )
            thumbs = thumbs_obj.thumbs
        except self.thumbs_cls.DoesNotExist:
            pass
        all_thumbs = self.thumbs_cls.objects.filter(panjivarecordid=self.object.panjivarecordid)

        flags = []
        try:
            flags_obj = Flags.objects.get(
                panjivarecordid=self.object.panjivarecordid)
            flags = flags_obj.to_pretty_list()
        except Flags.DoesNotExist:
            pass

        context.update({
            "hide_all": 'hide' in self.request.GET,
            "hide_compare": 'hide_compare' in self.request.GET,
            "comment": comment,
            "thumbs": thumbs,
            "flags": flags,
            "track_name": self.track_name,
            "all_comments": all_comments,
            "all_thumbs": all_thumbs
        })
        return context

    def render_to_response(self, context, *args, **kwargs):
        response = super().render_to_response(context, *args, **kwargs)
        response.render()
        return JsonResponse({
            'html': response.content.decode(response.charset)
        })


class ChinaImportExpandRowView(BaseExpandedRowView):
    transaction_cls = ChinaImport
    comment_cls = ChinaImportComment
    thumbs_cls = ChinaImportThumbs
    track_name = 'china_import'


class ChinaExportExpandRowView(BaseExpandedRowView):
    transaction_cls = ChinaExport
    comment_cls = ChinaExportComment
    thumbs_cls = ChinaExportThumbs
    track_name = 'china_export'


class PeruExportExpandRowView(BaseExpandedRowView):
    transaction_cls = PeruExport
    comment_cls = PeruExportComment
    thumbs_cls = PeruExportThumbs
    track_name = 'peru_export'


class UsImportExpandRowView(BaseExpandedRowView):
    transaction_cls = UsImport
    comment_cls = UsImportComment
    thumbs_cls = UsImportThumbs
    track_name = 'us_import'


class BaseUpdateView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])

    def post(self, request, track_name):
        if settings.DEBUG:
            print(request.POST)

        if track_name not in self.mapping:
            print("Figure out how to raise malformed request exception")
            return None

        object_cls, transaction_cls = self.mapping[track_name]
        transaction = transaction_cls.objects.using('wwf').get(panjivarecordid=request.POST['panjivarecordid'])

        obj = object_cls.objects.filter(
            panjivarecordid=transaction.panjivarecordid,
            user=request.user
        )
        if obj.exists():
            print("Trying to save changes")
            obj = obj[0]
            setattr(obj, self.value_attr, request.POST[self.value_key])
            obj.save()
        else:
            kwargs = {
                'panjivarecordid': transaction.panjivarecordid,
                'user': request.user,
                self.value_attr: request.POST[self.value_key]
            }
            object_cls.objects.create(**kwargs)
        return JsonResponse({
            'status': 'ok',
            self.value_attr: request.POST[self.value_key]  # this would need to prepend thumbs- if we care
        })


class SubmitThumbsView(BaseUpdateView):
    mapping = {
        'china_export': (ChinaExportThumbs, ChinaExport),
        'china_import': (ChinaImportThumbs, ChinaImport),
        'peru_export': (PeruExportThumbs, PeruExport),
        'us_import': (UsImportThumbs, UsImport),
    }
    value_attr = 'thumbs'
    value_key = 'value'


class SubmitCommentView(BaseUpdateView):
    mapping = {
        'china_export': (ChinaExportComment, ChinaExport),
        'china_import': (ChinaImportComment, ChinaImport),
        'peru_export': (PeruExportComment, PeruExport),
        'us_import': (UsImportComment, UsImport),
    }
    value_attr = 'comment'
    value_key = 'comment'

    def post(self, request, track_name):
        response = super(SubmitCommentView, self).post(request, track_name)
        body = json.loads(response.content)
        if 'status' in body and body['status'] == 'ok':
            rebuild_csv(track_name)
        return response


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


def get_results(request, track_name):
    print("Getting results")
    # all of these based on track_name
    trade_config = apps.get_app_config('trade')
    scores = trade_config.get_china_import()

    # ids = [160531980, 160531984, 160532111, 160532115, 160532119, 160532120, 160532127, 160532347, 160532348, 160532349]
    ids = [row[0] for row in scores][:1000]
    print("Came up with {} ids".format(len(scores)))

    model_cls = ChinaImport
    comment_cls = ChinaImportComment
    thumbs_cls = ChinaImportThumbs
    show_fields = ['shipmentmonth', 'consigneecountry', 'consigneepanjivaid', 'shipmentorigin', 'countryofsale', 'valueofgoodsusd', 'hscode']
    hidden_fields = ['consigneename', 'consigneecity', 'province', 'transportmethod', 'iscontainerized', 'adminregion', 'tradetype', 'hscodekeywords', 'panjivarecordid']

    scores = {pajiva_id: 1.0 for pajiva_id in ids}

    print("Got ids")

    comments = comment_cls.objects.filter(panjivarecordid__in=ids)
    comment_data = {comment.panjivarecordid: comment.comment for comment in comments}
    print("Massaged comments")

    thumbs = thumbs_cls.objects.filter(panjivarecordid__in=ids)
    thumbs_data = {thumb.panjivarecordid: thumb.thumbs for thumb in thumbs}
    print("Massaged thumbs")

    data = []
    for instance in model_cls.objects.using('wwf').filter(panjivarecordid__in=ids):
        data.append([
            scores[instance.panjivarecordid]
        ] + [
            format(instance, field) for field in show_fields
        ] + [
            format(instance, field) for field in hidden_fields
        ] + [
            comment_data[instance.panjivarecordid] if instance.panjivarecordid in comment_data else ''
        ] + [
            'thumbs-' + thumbs_data[instance.panjivarecordid] if instance.panjivarecordid in thumbs_data else ''
        ])

    print("Computed data")

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

    print("Sent")
    return JsonResponse({
        'columns': columns,
        'id_index': id_index,
        'hidden_cols': list(range(len(show_fields) + 1, len(fields) + 1)),
        'data': data,
    })
