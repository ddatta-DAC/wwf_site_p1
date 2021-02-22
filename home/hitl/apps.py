import os
import csv

from django.apps import AppConfig
from django.conf import settings


class HitlConfig(AppConfig):
    name = 'hitl'
    epochs = {}

    MAX_TRANSACTIONS = 50

    def load_csv(self, path):
        output = []
        epoch_file = os.path.join(settings.BASE_DIR, path)
        with open(epoch_file, 'r') as file:
            csvreader = csv.reader(file)
            next(csvreader)
            
            i = 0
            for row in csvreader:
                row[0] = int(float(row[0]))
                output.append(row)
                i += 1
                if i >= self.MAX_TRANSACTIONS:
                    break
        return output

    def get_epoch(self, path):
        if path not in self.epochs:
            self.epochs[path] = self.load_csv(path)
        return self.epochs[path]
