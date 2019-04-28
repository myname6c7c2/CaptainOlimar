from django.urls import path

from .views.pikmins.pikmins_view import index


app_name = 'pikmins'

urlpatterns = [
    path('', index, name='index'),
]
