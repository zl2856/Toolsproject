ifrom django.core.management.base import BaseCommand, CommandError
from sightings.models import Squirrel
import pandas as pd


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file_path', nargs='+', type=str, help="export a csv file")

    def handle(self, *args, **options):
        path = options['file_path'][0]
        df = pd.DataFrame(Squirrel.objects.all().values())
        df.replace('Other', '', inplace=True)
        df['Date'] = df['Date'].apply(lambda x: x.strftime("%m%d%Y"))
        df.to_csv(path, encoding='utf-8')
