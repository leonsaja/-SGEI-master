from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView,ListView,DeleteView,DetailView
from editais.forms import form_edital
from editais.models import Edital

class CriarEditalView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    form_class = form_edital.CriarEditalForm
    template_name ='edital/edital_form.html'
    success_url=reverse_lazy('edital:listar_editais')

class EditarEditalView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model = Edital
    form_class = form_edital.EditalEditalForm
    template_name = 'edital/edital_form.html'
    success_url = reverse_lazy('edital:listar_editais')
    success_message = 'Edital atualizado com sucesso'

class ListarEditalView(LoginRequiredMixin,ListView):

    model = Edital
    context_object_name = 'editais'
    template_name = 'edital/listar_editais.html'
    paginate_by =25

    def get_paginate_by(self, queryset):
        limit_page = self.request.GET.get('limit', '25')
        if not (limit_page.isdigit() and int(limit_page) > 0):
            limit_page = self.paginate_by
        quant=self.paginate_by=limit_page
        return quant

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super(ListarEditalView, self).get_context_data(**kwargs)
        context['quant_pages']=['10','15','25','35','50']
        context['limit_page']=self.paginate_by
        return context

class RemoverEditalView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    model = Edital
    template_name = 'edital/edital_confirm_delete.html'
    success_url = reverse_lazy('edital:listar_editais')
    success_message = 'Edital excluído com sucesso'

class DetalheEditalView(LoginRequiredMixin,SuccessMessageMixin,DetailView):
    model = Edital
    template_name = 'edital/edital_detail.html'

    def get_context_data(self, **kwargs):
        context=super(DetalheEditalView, self).get_context_data(**kwargs)
        context['edital'] =Edital.objects.get(pk=self.kwargs['pk'])
        return context



