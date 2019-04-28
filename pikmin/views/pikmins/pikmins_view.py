from django.shortcuts import render
from django.views.generic import ListView

from pikmin.models.pikmins.pikmin import Pikmin


class IndexView(ListView):

    model = Pikmin
    context_object_name = 'pikmins'
    template_name = 'pikmins/index.html'
    paginate_by = 5

index = IndexView.as_view()