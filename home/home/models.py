from django.conf import settings
from django.db import models
from django.utils import timezone
import pandas as pd
from django.db import models


# -----------
# Class to read in attributes on which to create Sankey diagram
# Ensure one entry for each data source
# -----------
class raw_data_model(models.Model):

    attr_dict = {
        'china_import': {
            'ShipmentOrigin': True,
            'CountryOfSale': True,
            'Province': True
        }
    }

    def __init__(self, data_source='china_import'):
        models.Model.__init__(self)
        self.data_source = 'china_import'
        self.attr_dict = dict(raw_data_model.attr_dict[self.data_source])
        return

    def get_attr_dict(self):
        return self.attr_dict

# -----------
