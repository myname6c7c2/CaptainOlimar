from django.shortcuts import render
from django.views.generic import ListView

from pikmin.forms.pikmins.pikmin_search_form import PikminSearchForm
from pikmin.models.pikmins.pikmin import Pikmin


class IndexView(ListView):

    model = Pikmin
    context_object_name = 'pikmins'
    template_name = 'pikmins/index.html'
    paginate_by = 5

    def post(self, request, *args, **kwargs):
        search_form = PikminSearchForm(request, prefix='search_form')


        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        search_form = PikminSearchForm()

        if 'search_form' in self.request.session:
            search_form = self.request.session['search_form']

        context['search_form'] = search_form

        return context

index = IndexView.as_view()