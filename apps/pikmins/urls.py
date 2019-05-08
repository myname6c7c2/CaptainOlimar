from django.urls import path

from .views import pikmins_view


app_name = 'pikmins'

urlpatterns = [
    path('', pikmins_view.index, name='pikmins_index'),
    path('pikmins/edit', pikmins_view.create, name='pikmins_create'),
    path('pikmins/edit/<int:pk>', pikmins_view.update, name='pikmins_update'),
]
