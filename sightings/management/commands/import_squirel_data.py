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
            if row['Age'] not in ['Adult', 'Juvenile']:
                # store squirrel's age = s_age
                s_age = Squirrel.Other
            else:
                s_age = row['Age']
  
            if row['Primary Fur Color'] not in ['Grey', 'Cinnamon', 'Black']:
                s_color = Squirrel.Other
            else:
                s_color = row['Primary Fur Color']

            if row['Location'] not in ['Ground Plane', 'Above Ground',]:
                s_location = Squirrel.Other
            else:
                s_location = row['Location']

            date = str(row['Date'])
            cn, created = Squirrel.objects.get_or_create(
                    latitude=row['Y'],
                    longitude=row['X'],
                    unique_Squirrel_id=row['Unique Squirrel ID'],
                    shift=row['Shift'],
                    date=datetime.date(int(date[4:]), int(date[:2]), int(date[2:4])),
                    age=s_age,
                    Primary_Fur_Color=s_color,
                    Location=s_location,
                    Specific_Location=row['Specific Location'],
                    Running=row['Running'],
                    Chasing=row['Chasing'],
                    Climbing=row['Climbing'],
                    Eating=row['Eating'],
                    Foraging=row['Foraging'],
                    Other_Activities=row['Other Activities'],
                    Kuks=row['Kuks'],
                    Quaas=row['Quaas'],
                    Moans=row['Moans'],
                    Tail_Flags=row['Tail flags'],
                    Tail_Twitches=row['Tail twitches'],
                    Approaches=row['Approaches'],
                    Indifferent=row['Indifferent'],
                    Runs_From=row['Runs from']
                    )
