import logging
import os
import yaml

from django.apps import AppConfig
from django.conf import settings


logger = logging.getLogger(__name__)


class HomeConfig(AppConfig):
    name = 'home'
    attrs = {}

    def ready(self):
        attrs_file = os.path.join(settings.BASE_DIR, 'home', 'attrs.yaml')

        with open(attrs_file, 'r') as stream:
            try:
                self.attrs = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    def get_attrs(self, topic):
        if topic not in self.attrs:
            logger.error("No {} in HomeConfig attrs".format(topic))
            return []

        return self.attrs[topic]['valid_cols']
