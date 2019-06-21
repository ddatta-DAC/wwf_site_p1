import logging
import os
import csv

from django.apps import AppConfig
from django.conf import settings


logger = logging.getLogger(__name__)


class TradeConfig(AppConfig):
    name = 'trade'
    china_import = None
    china_export = None
    peru_export = None
    us_import = None

    def load_csv(self, filename):
        output = []
        scores_file = os.path.join(settings.BASE_DIR, 'trade', 'data', filename)
        with open(scores_file, 'r') as file:
            csvreader = csv.reader(file)
            next(csvreader)
            for row in csvreader:
                output.append(row)
        return output

    def get_china_import(self):
        if self.china_import is None:
            self.china_import = self.load_csv('{}_scores.csv'.format('china_import'))
        return self.china_import

    def get_china_export(self):
        if self.china_export is None:
            self.china_export = self.load_csv('{}_scores.csv'.format('china_export'))
        return self.china_export

    def get_peru_export(self):
        if self.peru_export is None:
            self.peru_export = self.load_csv('{}_scores.csv'.format('peru_export'))
        return self.peru_export

    def get_us_import(self):
        if self.us_import is None:
            self.us_import = self.load_csv('{}_scores.csv'.format('us_import'))
        return self.us_import
