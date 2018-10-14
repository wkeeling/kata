from django.shortcuts import render

from championship.models import Season


def home_page(request):
    return render(request, 'home.html', {
        'season': Season.objects.first(),
        'navigation': [
            ('', 'Switch Season'),
            ('', 'Add Season')
        ]
    })


def add_season(request):
    return render(request, 'add_season.html')
