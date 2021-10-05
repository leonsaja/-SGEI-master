from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms

class LoginForm(AuthenticationForm):

    username = forms.EmailField()
    class Meta:
        model = get_user_model
        fields = ['username','password']

class EditarUserForm(UserChangeForm):
    password = None
    cpf=None

    class Meta:
        model = get_user_model()
        fields = ['nome','email','data_nascimento','telefone']


class CadastrarUserForm(UserCreationForm):
    cpf = forms.CharField(label='CPF', widget=forms.TextInput(attrs={'data-mask': "000.000.000-00"}))
    telefone = forms.CharField(label='Telefone', widget=forms.TextInput(attrs={'data-mask': "(00)00000-0000"}))

    class Meta:
        model= get_user_model()
        fields= ['username','nome','email','cpf','data_nascimento','telefone']

    def clean_telefone(self):
        data = self.cleaned_data['telefone']
        telefone = data.replace("(", "").replace(")", "").replace("-", "")

        return telefone

    def clean_cpf(self):
        data = self.cleaned_data['cpf']
        cpf = data.replace(".", "").replace("-", "")
        return cpf
