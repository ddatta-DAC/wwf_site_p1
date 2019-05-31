from django.http import JsonResponse, HttpResponseNotAllowed, Http404
from django.views import View
from django.views.generic.detail import DetailView

from .models import ChinaExport, PeruExport, UsImport, ChinaImport, ChinaExportComment, ChinaImportComment, PeruExportComment, UsImportComment, ChinaExportThumbs, ChinaImportThumbs, PeruExportThumbs, UsImportThumbs


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
                panjivarecordid=self.object.panjivarecordid)
            comment = comment_obj.comment
        except self.comment_cls.DoesNotExist:
            pass

        thumbs = 'clear'
        try:
            thumbs_obj = self.thumbs_cls.objects.get(
                panjivarecordid=self.object.panjivarecordid)
            thumbs = thumbs_obj.thumbs
        except self.thumbs_cls.DoesNotExist:
            pass

        context['comment'] = comment
        context['thumbs'] = thumbs

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


class BaseUpdateView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])

    def post(self, request, track_name):
        print(request.POST)

        if track_name not in self.mapping:
            print("Figure out how to raise malformed request exception")
            return None

        object_cls, transaction_cls = self.mapping[track_name]
        transaction = transaction_cls.objects.using('wwf').get(panjivarecordid=request.POST['panjivarecordid'])

        obj = object_cls.objects.filter(panjivarecordid=transaction.panjivarecordid)
        if obj.exists():
            print("Trying to save changes")
            obj = obj[0]
            setattr(obj, self.value_attr, request.POST[self.value_key])
            obj.save()
        else:
            kwargs = {
                'panjivarecordid': transaction.panjivarecordid,
                self.value_attr: request.POST[self.value_key]
            }
            object_cls.objects.create(**kwargs)
        return JsonResponse({
            'status': 'ok'
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
    # all of these based on track_name
    ids = [160531980, 160531984, 160532111, 160532115, 160532119, 160532120, 160532127, 160532347, 160532348, 160532349]
    model_cls = ChinaImport
    comment_cls = ChinaImportComment
    thumbs_cls = ChinaImportThumbs
    show_fields = ['shipmentmonth', 'consigneecountry', 'consigneepanjivaid', 'shipmentorigin', 'countryofsale', 'valueofgoodsusd', 'hscode']
    hidden_fields = ['consigneename', 'consigneecity', 'province', 'transportmethod', 'iscontainerized', 'adminregion', 'tradetype', 'hscodekeywords', 'panjivarecordid']

    scores = {pajiva_id: 1.0 for pajiva_id in ids}

    comments = comment_cls.objects.filter(panjivarecordid__in=ids)
    comment_data = {comment.panjivarecordid: comment.comment for comment in comments}

    thumbs = thumbs_cls.objects.filter(panjivarecordid__in=ids)
    thumbs_data = {thumb.panjivarecordid: thumb.thumbs for thumb in thumbs}

    data = []
    for pajiva_id in ids:
        instance = model_cls.objects.using('wwf').get(panjivarecordid=pajiva_id)

        data.append([
            scores[pajiva_id]
        ] + [
            format(instance, field) for field in show_fields
        ] + [
            format(instance, field) for field in hidden_fields
        ] + [
            comment_data[pajiva_id] if pajiva_id in comment_data else ''
        ] + [
            'thumbs-' + thumbs_data[pajiva_id] if pajiva_id in thumbs_data else ''
        ])

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

    return JsonResponse({
        'columns': columns,
        'id_index': id_index,
        'hidden_cols': list(range(len(show_fields) + 1, len(fields) + 1)),
        'data': data,
    })
