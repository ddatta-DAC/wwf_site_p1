from django.http import JsonResponse

from .models import ChinaImport


def get_results(request, track_name):
    # all of these based on track_name
    ids = [160531980, 160531984, 160532111, 160532115, 160532119, 160532120, 160532127, 160532347, 160532348, 160532349]
    model_cls = ChinaImport
    fields = ['shipmentmonth', 'consigneename', 'consigneecity', 'consigneecountry', 'consigneepanjivaid', 'shipmentorigin', 'province', 'countryofsale', 'transportmethod', 'iscontainerized', 'valueofgoodsusd', 'hscode', 'hscodekeywords', 'adminregion', 'tradetype']
    show_fields = ['shipmentmonth', 'consigneecountry', 'consigneepanjivaid', 'shipmentorigin', 'countryofsale', 'valueofgoodsusd', 'hscode'];
    expand_fields = ['consigneename', 'consigneecity', 'province', 'transportmethod', 'iscontainerized', 'hscodekeywords', 'adminregion', 'tradetype'];

    # fields = ['shipmentmonth', 'consigneecountry', 'consigneepanjivaid', 'shipmentorigin', 'countryofsale', 'valueofgoodsusd', 'hscode']

    data = []
    for pajiva_id in ids:
        instance = model_cls.objects.using('wwf').get(panjivarecordid=pajiva_id)

        data.append([
            getattr(instance, field, '') for field in fields
        ])

    return JsonResponse({
        'columns': fields,
        'main': show_fields,
        'expand': expand_fields,
        'data': data
    })
