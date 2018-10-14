from django.urls import path

import championship.views


urlpatterns = [
    path('', championship.views.home_page, name='home'),
    path('add$', championship.views.add_season, name='add_season'),
]
