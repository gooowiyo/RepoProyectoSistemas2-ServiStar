from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, OrdenServicio


class RegistroForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    rol = forms.ChoiceField(choices=Profile.ROLES)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'rol']

class OrdenServicioForm(forms.ModelForm):
    class Meta:
        model = OrdenServicio
        fields = '__all__'
        widgets = {
            'recepcion_fecha': forms.DateInput(attrs={'type': 'date'}),
            'recepcion_hora': forms.TimeInput(attrs={'type': 'time'}),
            'observaciones': forms.Textarea(attrs={'rows': 3}),
            'fecha_entrega': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        exclude = ['asesor', 'estado']