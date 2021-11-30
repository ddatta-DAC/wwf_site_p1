import os
import csv

from django.apps import AppConfig
from django.conf import settings
import logging

from sklearn.preprocessing import MinMaxScaler
import pandas as pd

logger = logging.getLogger(__name__)


class HitlConfig(AppConfig):
    name = 'hitl'
    epochs = {}
    onlineObj = None

    MAX_TRANSACTIONS = 50

    def ready(self):
        from PairwiseComparison.fetchRecord_details import setupGlobals, initialize
        from onlineUpdateModule.system_run import onlineUpdateExecutor
        from onlineUpdateModule  import data_handler


        base_path = "/home/django/Code/HITL_System_v0"

        logger.error("Starting data_handler.data_handler")
        data_handler_obj = data_handler.data_handler(
            DATA_LOC=f'{base_path}/generated_data_v1/us_import/',
            subDIR='01_2016',
            embedding_data_path=f'{base_path}/records2graph/saved_model_data',
            anomaly_result_dir=f'{base_path}/AD_model/combined_output',
            data_store_dir='./tmp'
        )

        logger.error("Starting onlineUpdateExecutor")
        self.onlineObj = onlineUpdateExecutor(
            data_handler_obj,
            update_at_every=4
        )

        
        logger.error("Starting pairwiseInitialize ")
        setupGlobals('{}/generated_data_v1/us_import'.format(base_path))
        logger.error("Not calling pairwise initialize should be remembered")
        # initialize(
        # )
        initialize(
            "{}/generated_data_v1/us_import/".format(base_path),
            "{}/PairwiseComparison/pairWiseDist/".format(base_path),
            "01_2016",
            _anomaly_result_dir='{}/AD_model/combined_output'.format(base_path),
            _result_pkl_cacheDir = 'pkl_Cache',
            load_redis = False
        )
        logger.error("Done with pairwise init")

    def load_csv(self, path):
        output = []
        # epoch_file = os.path.join(settings.BASE_DIR, path)
        epoch_file = os.path.join("/home/django/Code", path)
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
        epoch = self.load_csv("HITL_System_v0/AD_model/combined_output/01_2016/AD_output.csv")

        df = self.onlineObj.obtain_current_unlabelled_output()
        df = df[df["PanjivaRecordID"].isin([r[0] for r in epoch])].head(50)

        scaler = MinMaxScaler()
        scaler.fit(df['cur_score'].values.reshape([-1,1]))

        return zip(
            df["PanjivaRecordID"],
            scaler.transform(df['cur_score'].values.reshape([-1,1])).reshape(-1)
        )
