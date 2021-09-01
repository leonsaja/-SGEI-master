from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from accounts.models import User
from django.views.generic import ListView,CreateView,DetailView
from accounts.forms import form_user_admin


class CriarUsuarioAdminView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    form_class = form_user_admin.CadastrarUserAdminForm
    template_name = 'usuario/admin/form_admin.html'
    success_url = reverse_lazy('accounts:listar_usuarios')
    success_message = 'Usuario Cadastrado com sucesso'

class ListarUsuariosView(LoginRequiredMixin,ListView):

    model=User
    queryset =User.objects.filter(is_staff=False)
    context_object_name = 'usuarios'
    template_name = 'usuario/admin/listar_admin.html'
    paginate_by = 25

    def get_paginate_by(self, queryset):
        limit_page = self.request.GET.get('limit', '25')
        if not (limit_page.isdigit() and int(limit_page) > 0):
            limit_page = self.paginate_by
        quant = self.paginate_by = limit_page
        return quant

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListarUsuariosView, self).get_context_data(**kwargs)
        context['quant_pages'] = ['10', '15', '25', '35', '50']
        context['limit_page'] = self.paginate_by
        return context

class DetalheUuserView(LoginRequiredMixin,DetailView):
    pass