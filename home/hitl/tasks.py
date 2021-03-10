import os

from django.conf import settings
from django.core import management

from huey.contrib.djhuey import task, lock_task

initialized = False

@task()
@lock_task('initialize-lock')
def initialize():
    if not initialized:
        from VisualComponents_backend.TimeSeries import fetchTimeSeries as TS
        from VisualComponents_backend.EmbViz_all import main as embTSNE
        from PairwiseComparison.fetchRecord_details import initialize as pairwiseInitialize
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
        pairwiseInitialize(
                "{}/generated_data_v1/us_import/".format(base_path),
                "{}/PairwiseComparison/pairWiseDist/".format(base_path),
                "01_2016",
        )
        logger.error("Done with initializations {}".format(datetime.now()))

    initialized = True        

