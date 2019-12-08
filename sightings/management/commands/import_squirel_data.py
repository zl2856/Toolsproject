from django.core.management.base import BaseCommand, CommandError
from sightings.models import Squirrel
import pandas as pd
import datetime


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file_path', nargs=1, type=str, help='Path of data file')

    def handle(self, *args, **options):
        path = options['file_path'][0]

        df = pd.read_csv(path)

        for i in range(len(df)):
            row = df.loc[i]
            date = str(row['Date'])
            cn, created = Squirrel.objects.get_or_create(
                    latitude=row['Y'],
                    longitude=row['X'],
                    unique_squirrel_id=row['Unique Squirrel ID'],
                    shift=row['Shift'],
                    date=datetime.date(int(date[4:]), int(date[:2]), int(date[2:4])),
                    age=row['Age'],
                    primary_fur_color=row['Primary Fur Color'],
                    location=row['Location'],
                    specific_location=row['Specific Location'],
                    running=row['Running'],
                    chasing=row['Chasing'],
                    climbing=row['Climbing'],
                    eating=row['Eating'],
                    foraging=row['Foraging'],
                    other_activities=row['Other Activities'],
                    kuks=row['Kuks'],
                    quaas=row['Quaas'],
                    moans=row['Moans'],
                    tail_flags=row['Tail flags'],
                    tail_twitches=row['Tail twitches'],
                    approaches=row['Approaches'],
                    indifferent=row['Indifferent'],
                    runs_from=row['Runs from']
                    )
