import os

from django.conf import settings
from django.core import management

from huey.contrib.djhuey import db_task


@db_task()
def rebuild_csv(track_name):
    scores_file = os.path.join(settings.BASE_DIR, 'trade', 'data', 'v2', '{}_scores.csv'.format(track_name))

    management.call_command('build_csv', track_name, scores_file)
