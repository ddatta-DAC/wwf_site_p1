from django.views.generic.base import TemplateView
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.shortcuts import render
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

def data_home(request, route=None):
    route = request.GET.get('source')
    attr_list = ['a', 'b']

    print(request)

    # valid list of pages
    valid_list = ['china_import']

    if route not in valid_list:
        # Redirect to home
        response = redirect('/home')
        return response

    elif route == 'china_import':
        tmpl_data = processor_1.format_china_import()
        return render(
            request,
            "data_page.html",
            tmpl_data
        )

# ----------------
#
# ----------------
def viz_attr_selection(request):

    if request.method == 'POST':
        source = request.POST['source']
        # get the attributes
        print(request.POST)

        _dict = models.raw_data_model.attr_dict[source]
        post_keys = request.POST.keys()
        for k in _dict.keys():
            if k not in post_keys:
                _dict[k] = False
        print(_dict)
        # save _dict
        with open('viz_attr_dict.pkl','wb') as fh:
            pickle.dump(_dict,fh,pickle.HIGHEST_PROTOCOL)

        response = redirect('/track?source='+source)
        return response
    return

