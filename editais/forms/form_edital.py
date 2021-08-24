from django import  forms
from editais.models import Edital

class CriarEditalForm(forms.ModelForm):

    class Meta:
        model =Edital
        fields ='__all__'

class EditalEditalForm(forms.ModelForm):

    class Meta:
        model =Edital
        fields ='__all__'
