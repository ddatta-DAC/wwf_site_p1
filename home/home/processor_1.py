# file to get all the data
from . import models
import os
import pandas
import pickle

def format_china_import():
    tmpl_data = {}
    if not os.path.exists('viz_attr_dict.pkl'):
        obj_1 = models.raw_data_model('china_import')
        attr_dict = obj_1.get_attr_dict()
    else :
        with open('viz_attr_dict.pkl','rb') as fh:
            attr_dict = pickle.load(fh)
    print('-----')
    print(attr_dict)
    tmpl_data['attr_dict'] = attr_dict
    return tmpl_data