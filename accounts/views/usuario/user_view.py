from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView
from accounts.forms.usuario import form_user
from django.contrib.auth import get_user_model
from accounts.forms.usuario.perfil_form import PerfilForm

class CriarUsuarioView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    form_class = form_user.CadastrarUserForm
    template_name = 'user/form_user.html'
    success_url = reverse_lazy('accounts:listar_usuarios')
    success_message = 'Usuário cadastrado com sucesso!!'

class EditarUsuarioView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):

    model = get_user_model()
    form_class = form_user.EditarUserForm
    template_name = 'user/form_user.html'
    success_url = reverse_lazy('core:index')
    success_message = 'Usuário Atualizado com sucesso !!'

def perfil_user(request):

    if request.method == 'POST':
        form=PerfilForm(data=request.POST,instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('accounts:criar_usuario')
    else:
        form = PerfilForm(instance=request.user)

    return  render(request,'user/perfil_user.html',{'forms':form})