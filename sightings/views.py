from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.forms import ModelForm
from .models import Squirrel
from django.core.exceptions import ObjectDoesNotExist
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
    # get instance from database. If usid doesn't exist, program will raise a
    # DoesNotExist exception. 
    try:
        instance = Squirrel.objects.get(unique_squirrel_id=unique_squirrel_id)
    except ObjectDoesNotExist:
        err_msg = 'Instance squirrel <{}> doesn\'t exist'.format(unique_squirrel_id)
        return render(request, 'sightings/error.html', { 'error': err_msg })

    # get parameters
    if request.method == 'POST':
        usid = request.POST.get('unique_squirrel_id', '')
        form = SquirrelForm(request.POST, instance=instance)
    else:
        usid = reuqest.GET.get('unique_squirrel_id', '')
        form = SquirrelForm(instance=instance)

    # validate inputs
    if usid == '':
        return render(request, 'sightings/update.html', { 'form': form })
    elif form.is_valid():
        form.save()
    else:
        return render(request, 'sightings/error.html', { 'error': form.errors })

def add(request):
    if request.method == 'POST':
        usid = request.POST.get('unique_squirrel_id', '')
        form = SquirrelForm(request.POST)
    else:
        usid = reuqest.GET.get('unique_squirrel_id', '')
        form = SquirrelForm()



    if form.is_valid():
        squirrel = form.save()
        return JsonResponse({ 'success': True, 'error': None })
    return JsonResponse({ 'success': False, 'error': None })

def stats(reuqest):
    return render(request, 'sightings/index.html', context)
# Create your views here.
