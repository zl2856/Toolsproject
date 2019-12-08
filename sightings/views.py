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
        usid = request.GET.get('unique_squirrel_id', '')
        form = SquirrelForm(instance=instance)

    # handle request
    success_msg = 'Congradulations! Your record is updated.'
    return handleGeneralRequest(request, form, usid == '', unique_squirrel_id, success_msg)

def add(request):
    if request.method == 'POST':
        usid = request.POST.get('unique_squirrel_id', '')
        form = SquirrelForm(request.POST)
    else:
        usid = request.GET.get('unique_squirrel_id', '')
        form = SquirrelForm()

    # handle request
    success_msg = 'Congradulations! Your record is added.'
    return handleGeneralRequest(request, form, usid == '', 'add', success_msg)

def stats(request):
    stat = {
        'running_cnt': Squirrel.objects.filter(running=True).count(), 
        'chasing_cnt': Squirrel.objects.filter(chasing=True).count(), 
        'climbing_cnt': Squirrel.objects.filter(climbing=True).count(), 
        'eating_cnt': Squirrel.objects.filter(eating=True).count(), 
        'foraging_cnt': Squirrel.objects.filter(foraging=True).count(), 
    }
    print(stat)
    return render(request, 'sightings/stats.html', stat)

''' aux functions
'''
def handleGeneralRequest(request, form, render_blank_form, action_url, success_msg):
    # validate inputs
    if render_blank_form:
        return render(request, 'sightings/general.html', { 'url': action_url, 'form': form })
    elif form.is_valid():
        form.save()
        return render(request, 'sightings/success.html', { 'message': success_msg } )
    else:
        return render(request, 'sightings/error.html', { 'error': form.errors })
