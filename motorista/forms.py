from django import forms
from motorista.models import Motorista, Movimentacao

class MotoristaForm(forms.ModelForm):

    class Meta:
        model = Motorista
        fields = '__all__'