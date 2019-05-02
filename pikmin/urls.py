from django.urls import path

from .views.pikmins.pikmins_view import create, index, update


app_name = 'pikmins'

urlpatterns = [
    path('', index, name='index'),
    path('pikmins/edit', create, name='create'),
    path('pikmins/edit/<int:pk>', update, name='update'),
]
