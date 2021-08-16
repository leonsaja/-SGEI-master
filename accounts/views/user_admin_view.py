from django.shortcuts import render, redirect
from accounts.forms import form_user_admin
from django.contrib import  messages


def criar_usuario_admin(request):

    if request.method == 'POST':
        form =form_user_admin.CadastrarUserAdminForm(data=request.POST or None)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Cadastro realizado com sucesso !!')
            return redirect('core:index')
    else:
        form = form_user_admin.CadastrarUserAdminForm()
    return render(request,'user/admin/form_user_admin.html', {'form': form})