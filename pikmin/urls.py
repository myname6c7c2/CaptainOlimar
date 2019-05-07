from django.urls import path

from .views.pikmins import pikmins_view
from .views.planets import planets_view


app_name = 'pikmins'

urlpatterns = [
    path('', pikmins_view.index, name='index'),
    path('pikmins/edit', pikmins_view.create, name='create'),
    path('pikmins/edit/<int:pk>', pikmins_view.update, name='update'),
    path('planets', planets_view.index, name='planets_index'),
    path('planets/edit', planets_view.create, name='planets_create'),
    path('planets/edit/<int:pk>', planets_view.update, name='planets_update'),
]
