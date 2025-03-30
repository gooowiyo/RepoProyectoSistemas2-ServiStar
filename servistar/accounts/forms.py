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

            # Seccion Datos del Cliente y Vehiculo
            'recepcion_fecha': forms.DateInput(attrs={'type': 'date'}),
            'recepcion_hora': forms.TimeInput(attrs={'type': 'time'}),

            # Seccion Revision Tecnica
            'cambio_aceite_notas': forms.TextInput(attrs={'placeholder': 'Notas'}),
            'revision_nivelesLiquidos_notas': forms.TextInput(attrs={'placeholder': 'Notas'}),
            'lavado_notas': forms.TextInput(attrs={'placeholder': 'Notas'}),
            'engrase_notas': forms.TextInput(attrs={'placeholder': 'Notas'}),
            'motor_notas': forms.TextInput(attrs={'placeholder': 'Notas'}),
            'afinado_motor_notas': forms.TextInput(attrs={'placeholder': 'Notas'}),
            'revision_frenos_notas': forms.TextInput(attrs={'placeholder': 'Notas'}),
            'revision_embrague_notas': forms.TextInput(attrs={'placeholder': 'Notas'}),
            'revision_transmision_notas': forms.TextInput(attrs={'placeholder': 'Notas'}),
            'revision_diferencial_notas': forms.TextInput(attrs={'placeholder': 'Notas'}),
            'revision_crucetas_notas': forms.TextInput(attrs={'placeholder': 'Notas'}),
            'revision_suspensionDelantera_notas': forms.TextInput(attrs={'placeholder': 'Notas'}),
            'revision_suspensionTrasera_notas': forms.TextInput(attrs={'placeholder': 'Notas'}),
            'revision_amortiguadores_notas': forms.TextInput(attrs={'placeholder': 'Notas'}),
            'revision_sistemasDireccion_notas': forms.TextInput(attrs={'placeholder': 'Notas'}),
            'revision_rodamientosRuedas_notas': forms.TextInput(attrs={'placeholder': 'Notas'}),
            'revision_sistemaElectrico_notas': forms.TextInput(attrs={'placeholder': 'Notas'}),
            'alineado_notas': forms.TextInput(attrs={'placeholder': 'Notas'}),
            'balanceado_notas': forms.TextInput(attrs={'placeholder': 'Notas'}),
            'rotacion_notas': forms.TextInput(attrs={'placeholder': 'Notas'}),
            'alineado_faroles_notas': forms.TextInput(attrs={'placeholder': 'Notas'}),
            'ajuste_interior_notas': forms.TextInput(attrs={'placeholder': 'Notas'}),
            'ajuste_carroceria_notas': forms.TextInput(attrs={'placeholder': 'Notas'}),
            'revision_ruido_notas': forms.TextInput(attrs={'placeholder': 'Notas'}),
            'otros_notas': forms.TextInput(attrs={'placeholder': 'Notas'}),

            # Seccion Observaciones
            'observaciones': forms.Textarea(attrs={'rows': 3}),
            'fecha_entrega': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        exclude = ['asesor', 'estado']