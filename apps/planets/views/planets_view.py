from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from apps.planets.forms.planet_forms import (
    PlanetSearchForm,
    PlanetForm,
    onion_formset)
from apps.planets.models.planet import Planet


class IndexView(ListView):

    model = Planet
    context_object_name = 'planets'
    template_name = 'planets/index.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['onion_formset'] = onion_formset

        if 'form_data' in self.request.session:
            form_data = self.request.session['form_data']
            context['search_form'] = PlanetSearchForm(form_data)
        else:
            context['search_form'] = PlanetSearchForm()

        return context


class PlanetCreateView(LoginRequiredMixin, CreateView):
    model = Planet
    form_class = PlanetForm
    template_name = 'planets/edit.html'
    success_url = reverse_lazy('planets:planets_index')


class PlanetUpdateView(LoginRequiredMixin, UpdateView):
    model = Planet
    form_class = PlanetForm
    template_name = 'planets/edit.html'
    success_url = reverse_lazy('planets:planets_index')


index = IndexView.as_view()
create = PlanetCreateView.as_view()
update = PlanetUpdateView.as_view()