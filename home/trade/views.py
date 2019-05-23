from django.http import JsonResponse

from .models import ChinaImport


def format(instance, field):
    value = getattr(instance, field, '')
    if field in ['valueofgoodsusd']:
        return '${:,}'.format(value)
    if field in ['shipmentmonth']:
        return value.strftime('%Y/%m')
    return value


def get_results(request, track_name):
    # all of these based on track_name
    ids = [160531980, 160531984, 160532111, 160532115, 160532119, 160532120, 160532127, 160532347, 160532348, 160532349]
    model_cls = ChinaImport
    fields = ['shipmentmonth', 'consigneename', 'consigneecity', 'consigneepanjivaid', 'consigneecountry', 'shipmentorigin', 'province', 'countryofsale', 'transportmethod', 'iscontainerized', 'valueofgoodsusd', 'hscode', 'adminregion', 'tradetype', 'hscodekeywords']
    show_fields = ['score', 'shipmentmonth', 'consigneecountry', 'consigneepanjivaid', 'shipmentorigin', 'countryofsale', 'valueofgoodsusd', 'hscode'];
    expand_fields = ['consigneename', 'consigneecity', 'province', 'transportmethod', 'iscontainerized', 'adminregion', 'tradetype', 'hscodekeywords'];

    scores = {pajiva_id: 1.0 for pajiva_id in ids}

    # fields = ['shipmentmonth', 'consigneecountry', 'consigneepanjivaid', 'shipmentorigin', 'countryofsale', 'valueofgoodsusd', 'hscode']

    data = []
    for pajiva_id in ids:
        instance = model_cls.objects.using('wwf').get(panjivarecordid=pajiva_id)

        data.append([scores[pajiva_id]] + [
            format(instance, field) for field in fields
        ])

    fields = ['score'] + fields

    return JsonResponse({
        'columns': fields,
        'main': show_fields,
        'expand': expand_fields,
        'data': data
    })
