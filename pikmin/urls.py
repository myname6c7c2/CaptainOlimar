from django.urls import path

from .views.pikmin_list.pikmin_list_view import index


app_name = 'pikmin'

urlpatterns = [
    path('list', index, name='index'),
]
