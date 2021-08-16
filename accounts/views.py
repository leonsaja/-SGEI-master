from django.contrib import  messages
from django.shortcuts import render, redirect
from accounts.forms.form_user import CadastrarUserForm,EditarUserForm
from django.contrib.auth import  get_user_model

def criar_usuario(request):

    if request.method == 'POST':
        form = CadastrarUserForm(data=request.POST or None)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Cadastro realizado com sucesso !!')
            return redirect('core:index')

    else:
        form = CadastrarUserForm()
    return render(request,'user/form_user.html', {'form': form})


def editar_usuario(request,id):

    User = get_user_model()
    user = User.objects.get(id=id)
    form = EditarUserForm(data=request.POST or None, instance=user)
    if request.method == 'POST':
        form = EditarUserForm(data=request.POST or None,instance=user)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Cadastro alterado com sucesso !!')
            return  redirect('core:index')
    else:
        form=EditarUserForm(data=request.POST or None, instance=user)
    return render(request,'user/form_user.html',{'form':form})