from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.forms import ModelForm
from .models import Squirrel
from django.utils.translation import gettext_lazy as _

class SquirrelForm(ModelForm):
    class Meta:
        model = Squirrel
        fields = ('latitude', 'longitude', 'unique_squirrel_id', 'shift', 'date', 
                'age', 'primary_fur_color', 'location', 'specific_location', 'running', 
                'chasing', 'climbing', 'eating', 'foraging', 'other_activities', 
                'kuks', 'quaas', 'moans', 'tail_flags', 'tail_twitches',
                'approaches', 'indifferent', 'runs_from')
        labels = {'latitude': _('Latitude'), 'longitude': _('Longitude'), 
                'unique_squirrel_id': _('USID'), 'shift': _('Shift'), 
                'date': _('Date'), 'age': _('Age'), 
                'primary_fur_color': _('Primary fur color'), 'location': _('Location'), 
                'specific_location': _('Specific location'), 'running': _('Running'), 
                'chasing': _('Chasing'), 'climbing': _('Climbing'), 
                'eating': _('Eating'), 'foraging': _('Foraging'), 
                'other_activities': _('Other activities'), 'kuks': _('Kuks'), 
                'quaas': _('Quaas'), 'moans': _('Moans'), 
                'tail_flags': _('Tail flags'), 'tail_twitches': _('Tail twitches'),
                'approaches': _('Approaches'), 'indifferent': _('Indifferent'), 
                'runs_from': _('Runs from')}

def list(request):
    context = {
        'squirrels': Squirrel.objects.all(),
    }
    return render(request, 'sightings/index.html', context)


def update(request, unique_squirrel_id):
    instance = Squirrel.objects.get(unique_squirrel_id=unique_squirrel_id)
    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance=instance)
    else:
        form = SquirrelForm(instance=instance)
    
    if form.is_valid():
        form.save()
        return JsonResponse({ 'success': True, 'error': None })
    else:
        return JsonResponse({ 'success': True, 'error': None })

def create(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
    else:
        form = SquirrelForm()

    if form.is_valid():
        squirrel = form.save()
        return JsonResponse({ 'success': True, 'error': None })
    return JsonResponse({ 'success': False, 'error': None })

def stats(reuqest):
    return render(request, 'sightings/index.html', context)
# Create your views here.
