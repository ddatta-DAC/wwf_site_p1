import csv
import json

from django.conf import settings
from django.core.management.base import BaseCommand

from .parsers import ChinaImportParser, ChinaExportParser, PeruExportParser, UsImportParser


class Command(BaseCommand):
    """Builds the csv for running the anomaly table.

    Example:
    ./manage.py build_china_import_csv china_import trade/data/china_import_scores.csv
    """

    help = 'Builds the csv for the output file'

    def add_arguments(self, parser):
        parser.add_argument('track', type=str)
        parser.add_argument('path', type=str)

    def handle(self, *args, **options):
        if options['track'] == 'china_import':
            parser_cls = ChinaImportParser
        elif options['track'] == 'china_export':
            parser_cls = ChinaExportParser
        elif options['track'] == 'peru_export':
            parser_cls = PeruExportParser
        elif options['track'] == 'us_import':
            parser_cls = UsImportParser
        else:
            self.stdout.write(self.style.ERROR('Unknown track type {}'.format(options['track'])))
            return

        with open(options['path']) as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            parser = parser_cls(reader)
            output = parser.process_scores()

            outfilepath = settings.ROOT_DIR + 'home' + settings.STATIC_ROOT + '{}.json'.format(options['track'])
            with open(outfilepath, 'w') as outfile:
                json.dump(output, outfile)

            self.stdout.write(self.style.SUCCESS('Successfully wrote to file "%s"' % outfilepath))
