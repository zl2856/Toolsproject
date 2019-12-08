from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    # choice definitions
    AM, PM = 'AM', 'PM'
    ADULT, JUVENILE, OTHER = 'Adult', 'Juvenile', 'Other'
    GRAY, CINNAMON, BLACK = 'Gray', 'Cinnamon', 'Black'
    GROUND, ABOVE = 'Ground Plane', 'Above Plane'
    SHIFT_CHOICE = [
            (AM, 'AM'),
            (PM, 'PM'),
    ]
    AGE_CHOICE = [
        (ADULT, 'Adult'),
        (JUVENILE, 'Juvenile'),
        (OTHER, 'Other'),
    ]
    COLOR_CHOICE = [
        (GRAY, 'Gary'),
        (CINNAMON, 'Cinnamon'),
        (BLACK, 'Black'),
        (OTHER, 'Other'),
    ]
    LOCATION_CHOICE = [
        (GROUND, 'Ground Plane'),
        (ABOVE, 'Above Plane'),
        (OTHER, 'Other'),
    ]

    # model members
    latitude = models.FloatField(help_text=_('Latitude of squirrels'))
    longitude = models.FloatField(help_text=_('Longitude of squirrels'))
    unique_squirrel_id = models.CharField(
        max_length=100, 
        help_text=_('Id of squirrels')
    )
    shift = models.CharField(
        max_length=2,
        choices=SHIFT_CHOICE,
        default=AM,
        help_text=_('AM/PM of sighting'),
    )
    date = models.DateField(help_text=_('Date'))
    age = models.CharField(
        max_length=10,
        choices=AGE_CHOICE,
        default=JUVENILE,
        help_text=_('Type of squirrel'),
    )
    primary_fur_color = models.CharField(
        max_length=10,
        choices=COLOR_CHOICE,
        default=CINNAMON,
        help_text=_('Color of squirrels'),
    )
    location = models.CharField(
        max_length=15,
        choices=LOCATION_CHOICE,
        default=GROUND,
        help_text=_('Location of first appearance'),
    )
    specific_location = models.CharField(
        max_length=256,
        help_text=_('Location description'),
    )
    running = models.BooleanField(
        default=False,
        help_text=_('Whether the squirrel was running'),
    )
    chasing = models.BooleanField(
        default=False,
        help_text=_('Whether the squirrel was chasing'),
    )
    climbing = models.BooleanField(
        default=False,
        help_text=_('Whether the squirrel was climbing'),
    )
    eating = models.BooleanField(
        help_text=_('Whether the squirrel was eating'),
        default=False,
    )
    foraging = models.BooleanField(
        default=False,
        help_text=_('Whether the squirrel was foraging'),
    )
    other_activities = models.CharField(
        max_length=256,
        help_text=_('Other activies'),
    )
    kuks = models.BooleanField(
        default=False,
        help_text=_('Whether the squirrel was heard kukking'),
    )
    quaas = models.BooleanField(
        default=False,
        help_text=_('Whether the squirrel was heard quaaing'),
    )
    moans = models.BooleanFiel(
        default=False,
        help_text=_('Whether the squirrel was heard moaning'),
    )
    tail_flags = models.BooleanField(
        default=False,
        help_text=_('Whether the squirrel was seen flagging its tail'),
    )
    tail_twitches = models.BooleanField(
        default=False,
        help_text=_('Whether the squirrel was seen twitching its tail'),
    )
    approaches = models.BooleanField(
        default=False,
        help_text=_('Whether the squirrel was seen approaching to human'),
    )
    indifferent = models.BooleanField(
        default=False,
        help_text=_('Whether the squirrel was indifferent to human presence'),
    )
    runs_from = models.BooleanField(
        default=False,
        help_text=_('Whether the squirrel was seen running from humans'),
    )

    def __str__(self):
        return self.unique_squirrel_id
# Create your models here.
