from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from sightings.models import Squirrel

def map(request):
    context = {
        'squirrels': Squirrel.objects.all(),
    }
    return render(request, 'map/map.html', context)
