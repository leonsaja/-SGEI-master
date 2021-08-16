from django.forms import  forms
from  django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth import  get_user_model

class CadastrarUserAdminForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['nome','email','cpf','data_nascimento','telefone','is_staff','is_superuser']