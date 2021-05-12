from django import forms
from motorista.models import Motorista, Movimentacao

class MotoristaForm(forms.ModelForm):

    class Meta:
        model = Motorista
        fields = '__all__'

class MovimentacaoForm(forms.ModelForm):

    class Meta:
        model = Movimentacao
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        hidden = kwargs.pop('hidden', None)
        super(MovimentacaoForm, self).__init__(*args, **kwargs)
        if hidden:
            self.fields['motorista'] = forms.ModelChoiceField(queryset=Motorista.objects.all(), widget=forms.HiddenInput,)