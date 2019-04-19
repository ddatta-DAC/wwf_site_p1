from django.views.generic.base import TemplateView
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.apps import apps

import sys
import os
sys.path.append('./../..')
from . import models
from . import processor_1
from django import forms
import pickle
# -----------------
#  HOME
# -----------------

def home(request):
    attr_list = ['a', 'b']
    return render(
        request,
        "index.html",
        {'attr_list': attr_list}
    )


# -----------------
# DATA
# -----------------

def data_home(request, track_name):
    # track_name will be one of {china_import, china_export, us_import, peru_export}
    # see home/templates/navigation.html

    home_config = apps.get_app_config('home')
    attrs = home_config.get_attrs(track_name)
    if not attrs:
        raise Http404

    context = {
        'attrs': attrs,
        'chk': True
    }

    # elif track_name == 'china_import':
    #     tmpl_data = processor_1.format_china_import()
    return render(
        request,
        "data_page.html",
        context
    )

# ----------------
#
# ----------------
def viz_attr_selection(request):
    if request.method == 'GET':
        # source = request.POST['source']
        # get the attributes
        print(request.GET)

        data = []
        # TODO get the real data for the requested attrs
        for attr in request.GET.getlist('attrs[]'):
            data.append([attr, 'foo', 'bar', 'baz']) # idk how this should be formatted

        # _dict = models.raw_data_model.attr_dict[source]
        # post_keys = request.POST.keys()
        # for k in _dict.keys():
        #     if k not in post_keys:
        #         _dict[k] = False
        # print(_dict)
        # # save _dict
        # with open('viz_attr_dict.pkl','wb') as fh:
        #     pickle.dump(_dict,fh,pickle.HIGHEST_PROTOCOL)

        # response = redirect('/track?source='+source)
        # return response
        return JsonResponse({'data': data})
    return

