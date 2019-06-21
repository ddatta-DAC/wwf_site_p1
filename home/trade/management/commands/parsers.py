from trade.models import ChinaImport, ChinaImportComment, ChinaImportThumbs, ChinaExport, ChinaExportComment, ChinaExportThumbs, PeruExport, PeruExportComment, PeruExportThumbs, UsImport, UsImportComment, UsImportThumbs


def custom_format(instance, field):
    value = getattr(instance, field, '')
    if field in ['valueofgoodsusd', 'valueofgoodsfobusd']:
        return '${:,.0f}'.format(value)
    if field in ['shipmentmonth']:
        return value.strftime('%Y/%m')
    if field in ['receiptdeclarationdate', 'arrivaldate']:
        return value.strftime('%Y/%m/%d')
    return value


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
    'panjivarecordid': 'panjivarecordid',
    'shipperpanjivaid': 'Shipper',
    'shipmentdestination': 'Destination',
    'valueofgoodsfobusd': 'Value FOB',
    'volumeteu': 'TEU',
    'receiptdeclarationdate': 'Declaration',
    'exportquantity': 'Quantity',
    'exportunit': 'Unit',
    'arrivaldate': 'Arrival',
}


class BaseParser(object):
    """Call subclass(iterable of rows from csv) then obj.process_scores."""

    scores = {}

    def __init__(self, iterable):
        super(BaseParser, self).__init__()

        self.scores = {}
        for row in iterable:
            self.scores[row[0]] = row

    def process_scores(self, skip_scores=False):
        ids = list(self.scores.keys())[:10000]

        print("Got ids")

        comments = self.comment_cls.objects.filter(panjivarecordid__in=ids)
        comment_data = {comment.panjivarecordid: comment.comment for comment in comments}
        print("Massaged comments")

        thumbs = self.thumbs_cls.objects.filter(panjivarecordid__in=ids)
        thumbs_data = {thumb.panjivarecordid: thumb.thumbs for thumb in thumbs}
        print("Massaged thumbs")

        data = []
        for instance in self.model_cls.objects.using('wwf').filter(panjivarecordid__in=ids):
            score_value = ['{:.3f}'.format(float(self.scores[str(instance.panjivarecordid)][1]))]
            if skip_scores:
                score_value = []

            data.append(score_value + [
                custom_format(instance, field) for field in self.show_fields
            ] + [
                custom_format(instance, field) for field in self.hidden_fields
            ] + [
                comment_data[instance.panjivarecordid] if instance.panjivarecordid in comment_data else ''
            ] + [
                'thumbs-' + thumbs_data[instance.panjivarecordid] if instance.panjivarecordid in thumbs_data else ''
            ])

        print("Computed data")
        # print(data)

        score_field = ['score']
        if skip_scores:
            score_field = []

        fields = score_field + self.show_fields + self.hidden_fields + ['comment', 'thumbs']
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


        hidden_cols = list(range(len(self.show_fields) + 2, len(fields) + 1))
        if skip_scores:
            hidden_cols.insert(0, hidden_cols[0] - 1)

        output = {
            'columns': columns,
            'id_index': id_index,
            'hidden_cols': hidden_cols,
            'data': data,
        }

        return output


class ChinaImportParser(BaseParser):
    model_cls = ChinaImport
    comment_cls = ChinaImportComment
    thumbs_cls = ChinaImportThumbs
    show_fields = ['shipmentmonth', 'consigneecountry', 'consigneepanjivaid', 'shipmentorigin', 'countryofsale', 'hscode', 'valueofgoodsusd']
    hidden_fields = ['consigneename', 'consigneecity', 'province', 'transportmethod', 'iscontainerized', 'adminregion', 'tradetype', 'hscodekeywords', 'panjivarecordid']


class ChinaExportParser(BaseParser):
    model_cls = ChinaExport
    comment_cls = ChinaExportComment
    thumbs_cls = ChinaExportThumbs
    show_fields = [
        'shipmentmonth',
        'shipperpanjivaid',
        'shipmentdestination',
        'countryofsale',
        'hscode',
        'valueofgoodsusd'
    ]
    hidden_fields = [
        'shippername',
        'shipperultimateparentname',
        'transportmethod',
        'iscontainerized',
        'adminregion',
        'tradetype',
        'hscodekeywords',
        'panjivarecordid'
    ]


class PeruExportParser(BaseParser):
    model_cls = PeruExport
    comment_cls = PeruExportComment
    thumbs_cls = PeruExportThumbs
    show_fields = [
        'receiptdeclarationdate',
        'shipmentdestination',
        'hscode',
        'volumeteu',
        'valueofgoodsfobusd',
        'exportquantity',
        'exportunit'
    ]
    hidden_fields = [
        'shippername',
        'shippercity',
        'shipperstateregion',
        'shippercountry',
        'shipperultimateparentname',
        'portofunlading',
        'portofunladingcountry',
        'goodsshipped',
        'itemquantity',
        'grossweightkg',
        'netweightkg',
        'transportmethod',
        'iscontainerized',
        'panjivarecordid'
    ]


class UsImportParser(BaseParser):
    model_cls = UsImport
    comment_cls = UsImportComment
    thumbs_cls = UsImportThumbs
    show_fields = [
        'arrivaldate',
        'consigneepanjivaid',
        'shipperpanjivaid',
        'shipmentorigin',
        'shipmentdestination',
        'hscode',
        'volumeteu',
    ]
    hidden_fields = [
        'consigneename',
        'consigneecity',
        'consigneecountry',
        'consigneeultimateparentname',
        'portofunlading',
        'portoflading',
        'carrier',
        'placeofreceipt',
        'weightkg',
        'haslcl',
        'dividedlcl',
        'containernumbers',
        'goodsshipped',
        'panjivarecordid'
    ]
