import os
import csv

from django.apps import AppConfig
from django.conf import settings


class HitlConfig(AppConfig):
    name = 'hitl'
    epochs = {}

    TS = None
    embTSNE = None

    MAX_TRANSACTIONS = 50

    def ready(self):
        from VisualComponents_backend.TimeSeries import fetchTimeSeries as TS
        from VisualComponents_backend.EmbViz_all import main as embTSNE

        base_path = "/home/django/Code/HITL_System_v0"
        self.TS.initialize(_DATA_LOC="{}/generated_data_v1/us_import/".format(base_path), _subDIR='01_2016', _html_saveDir='{}/htmlCache'.format(base_path), _json_saveDir='{}/jsonCache'.format(base_path))
        self.embTSNE.initialize(
                _DATA_LOC='{}/generated_data_v1/us_import'.format(base_path),
                _subDIR='01_2016',
                mp2v_emb_dir = '{}/records2graph/saved_model_data'.format(base_path),
                emb_dim = 64,
                _htmlSaveDir = '{}/htmlCache'.format(base_path)
        )

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
