from django.shortcuts import render
from django.views.generic.edit import CreateView

from championship.models import Season


def home_page(request):
    return render(request, 'home.html', {
        'season': Season.objects.first(),
        'navigation': [
            ('', 'Switch Season'),
            ('add', 'Add Season')
        ]
    })


def add_season(request):
    return render(request, 'add_season.html', {
        'navigation': [
            ('', 'Add Driver'),
            ('add', 'Add Team')
        ]
    })
