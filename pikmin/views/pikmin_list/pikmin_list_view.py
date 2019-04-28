from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    
    template_name = 'pikmin/pikmin_list/index.html'

index = IndexView.as_view()