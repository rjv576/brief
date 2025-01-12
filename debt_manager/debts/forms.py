from django import forms
from .models import Debt

class DebtForm(forms.ModelForm):
    due_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control',  # Opcional: para estilos CSS como Bootstrap
                'placeholder': 'Seleccione una fecha'
            }
        )
    )
    
    class Meta:
        model = Debt
        fields = ['name', 'total_amount', 'interest_rate', 'minimum_payment', 'due_date']