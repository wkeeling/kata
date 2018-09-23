from django.urls import path

import championship.views


urlpatterns = [
    path('', championship.views.home_page, name='home'),
]
