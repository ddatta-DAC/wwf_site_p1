import logging
import os
import csv

from django.apps import AppConfig
from django.conf import settings


logger = logging.getLogger(__name__)


class TradeConfig(AppConfig):
    name = 'trade'
    china_import = []

    def ready(self):
        scores_file = os.path.join(settings.BASE_DIR, 'trade', 'data', 'china_import_scores.csv')

        with open(scores_file, 'r') as file:
            csvreader = csv.reader(file)
            next(csvreader)
            for row in csvreader:
                self.china_import.append(row)

    def get_china_import(self):
        return self.china_import
