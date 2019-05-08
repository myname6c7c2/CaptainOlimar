from django.urls import path

from .views.planets_view import create, index, update


app_name = 'planets'

urlpatterns = [
    path('', index, name='planets_index'),
    path('edit/', create, name='planets_create'),
    path('edit/<int:pk>', update, name='planets_update'),
]
