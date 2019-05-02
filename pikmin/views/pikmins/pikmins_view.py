from django.db.models import Q
from django.shortcuts import redirect, render
from django.views.generic import ListView

from pikmin.forms.pikmins.pikmin_search_form import PikminSearchForm
from pikmin.models.pikmins.pikmin import Pikmin


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

        form_data = self.request.session['form_data']

        if form_data:
            search_form = PikminSearchForm(form_data)
        else:
            search_form = PikminSearchForm()

        context['search_form'] = search_form

        return context

    def get_queryset(self):
        form_data = self.request.session['form_data']

        pikmins = Pikmin.objects.all()

        if form_data:
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

index = IndexView.as_view()