import os
import csv

from django.apps import AppConfig
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


class HitlConfig(AppConfig):
    name = 'hitl'
    epochs = {}

    MAX_TRANSACTIONS = 50

    def ready(self):
        # return
        from VisualComponents_backend.TimeSeries import fetchTimeSeries as TS
        from VisualComponents_backend.EmbViz_all import main as embTSNE
        from PairwiseComparison.fetchRecord_details import setupGlobals
        from VisualComponents_backend.StackedComparison.stackedComparison import initialize
        from VisualComponents_backend.HSCodeViz.main import initialize as hs_initialize
        from VisualComponents_backend.sankey_diagram.main import initialize as sankey_initialize
        # from VisualComponents_backend.companyNetworkViz.main import initialize as network_initialize

        from datetime import datetime

        logger.error("Starting TS {}".format(datetime.now()))
        base_path = "/home/django/Code/HITL_System_v0"
        TS.initialize(_DATA_LOC="{}/generated_data_v1/us_import/".format(base_path),
                _subDIR='01_2016',
                _html_saveDir='{}/htmlCache'.format(base_path), 
                _json_saveDir='{}/jsonCache'.format(base_path)
        )
        logger.error("Starting embTSNE {}".format(datetime.now()))
        embTSNE.initialize(
                _DATA_LOC='{}/generated_data_v1/us_import'.format(base_path),
                _subDIR='01_2016',
                mp2v_emb_dir = '{}/records2graph/saved_model_data'.format(base_path),
                emb_dim = 64,
                _htmlSaveDir = '{}/htmlCache'.format(base_path)
        )
        logger.error("Starting pairwiseInitialize {}".format(datetime.now()))
        setupGlobals('{}/generated_data_v1/us_import'.format(base_path))
        #pairwiseInitialize(
        #        "{}/generated_data_v1/us_import/".format(base_path),
        #        "{}/PairwiseComparison/pairWiseDist/".format(base_path),
        #        "01_2016",
        #)

        logger.error("Starting stacked initialization {}".format(datetime.now()))
        initialize(
            _DATA_LOC = '{}/generated_data_v1/us_import'.format(base_path),
            _subDIR = '01_2016',
            mp2v_emb_dir = '{}/records2graph/saved_model_data'.format(base_path),
            emb_dim = 64,
            _htmlSaveDir = '{}/htmlCache'.format(base_path)
        )

        logger.error("Starting hs initialization {}".format(datetime.now()))
        hs_initialize(
            _DATA_LOC='{}/generated_data_v1/us_import'.format(base_path),
            _subDIR='01_2016'
        )

        logger.error("Starting sankey initialization {}".format(datetime.now()))
        sankey_initialize(
            _DATA_LOC='{}/generated_data_v1/us_import'.format(base_path),
            _subDIR='01_2016',
            _html_saveDir='{}/htmlCache'.format(base_path),
            _json_saveDir='{}/jsonCache'.format(base_path)
        )

        logger.error("Starting network initialization {}".format(datetime.now()))
        # network_initialize(
        #     _DATA_LOC ='{}/generated_data_v1/us_import'.format(base_path),
        #     _saved_emb_loc =  '{}/GNN/saved_model_gnn'.format(base_path),
        #     _subDIR = '01_2016',
        #     _html_cache= '{}/htmlCache'.format(base_path),
        #     _df_cache = '{}/dfCache'.format(base_path),
        #     db_loc ='{}/DB/wwf.db'.format(base_path)
        # )

        logger.error("Done with initializations")

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
