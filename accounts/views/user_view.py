from django.contrib import messages
from django.shortcuts import render, redirect
from accounts.forms import form_user
from django.contrib.auth import get_user_model
from accounts.forms.perfil_form import PerfilForm
def criar_usuario(request):

    if request.method == 'POST':
        form = form_user.CadastrarUserForm(data=request.POST or None)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Cadastro realizado com sucesso !!')
            return redirect('core:index')
    else:
        form = form_user.CadastrarUserForm()
    return render(request,'user/form_user.html', {'form': form})

def editar_usuario(request,id):

    User = get_user_model()
    user = User.objects.get(id=id)
    if request.method == 'POST':
        form = form_user.EditarUserForm(data=request.POST or None,instance=user)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Cadastro alterado com sucesso !!')
            return  redirect('core:index')
    else:
        form=form_user.EditarUserForm(data=request.POST or None, instance=user)
    return render(request,'user/form_user.html',{'form':form})

def listar_usuarios(request):

    User=get_user_model()
    usuarios=User.objects.filter(is_staff=True)
    return render(request,'user/listar_usuarios.html',{'usuarios':usuarios})

def perfil_user(request):

    if request.method == 'POST':
        form=PerfilForm(data=request.POST,instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('accounts:criar_usuario')
    else:
        form = PerfilForm(instance=request.user)

    return  render(request,'user/perfil_user.html',{'form':form})