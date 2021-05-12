from django import forms
from empresa.models import Unidade

class UnidadeForm(forms.ModelForm):

    class Meta:
        model = Unidade
        fields = '__all__'