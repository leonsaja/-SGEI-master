from django.forms import  forms
from  django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth import  get_user_model
from django import  forms

class CadastrarUserAdminForm(UserCreationForm):
    cpf = forms.CharField(label='CPF', widget=forms.TextInput(attrs={'data-mask': "000.000.000-00"}))
    telefone = forms.CharField(label='Telefone', widget=forms.TextInput(attrs={'data-mask': "(00)00000-0000"}))

    class Meta:
        model = get_user_model()
        fields = ['username','nome','email','cpf','data_nascimento','telefone','is_staff','is_superuser']

    def clean_telefone(self):
        data = self.cleaned_data['telefone']
        telefone = data.replace("(", "").replace(")", "").replace("-", "")

        return telefone

    def clean_cpf(self):
        data = self.cleaned_data['cpf']
        cpf = data.replace(".", "").replace("-", "")
        return cpf


