from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from apps.pikmins.forms.pikmin_forms import (PikminSearchForm, PikminForm)
from apps.pikmins.models.pikmin import Pikmin


class IndexView(ListView):

    model = Pikmin
    context_object_name = 'pikmins'
    template_name = 'pikmins/index.html'
    paginate_by = 5

    def post(self, request, *args, **kwargs):
        search_form = PikminSearchForm(request.POST)

        if search_form.is_valid():
            request.session['form_data'] = request.POST

            return redirect('pikmins:index')

        context = {'search_form': search_form}

        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if 'form_data' in self.request.session:
            form_data = self.request.session['form_data']
            context['search_form'] = PikminSearchForm(form_data)
        else:
            context['search_form'] = PikminSearchForm()

        return context

    def get_queryset(self):

        pikmins = Pikmin.objects.all()

        if 'form_data' in self.request.session:
            form_data = self.request.session['form_data']
            condition = Q()

            if form_data['first_name']:
                condition &= Q(first_name__contains=form_data['first_name'])
            if form_data['last_name']:
                condition &= Q(last_name__contains=form_data['last_name'])
            if form_data['first_name_kana']:
                condition &= Q(first_name_kana__contains=form_data['first_name_kana'])
            if form_data['last_name_kana']:
                condition &= Q(last_name_kana__contains=form_data['last_name_kana'])
            if form_data['sex'] != '0':
                condition &= Q(sex=form_data['sex'])

            pikmins = pikmins.filter(condition)
        
        return pikmins.order_by('-pk')


class PikminCreateView(LoginRequiredMixin, CreateView):
    model = Pikmin
    form_class = PikminForm
    template_name = 'pikmins/edit.html'
    success_url = reverse_lazy('pikmins:index')


class PikminUpdateView(LoginRequiredMixin, UpdateView):
    model = Pikmin
    form_class = PikminForm
    template_name = 'pikmins/edit.html'
    success_url = reverse_lazy('pikmins:index')


index = IndexView.as_view()
create = PikminCreateView.as_view()
update = PikminUpdateView.as_view()