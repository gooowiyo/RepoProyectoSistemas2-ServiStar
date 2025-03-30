from django.shortcuts import render, redirect
from .forms import RegistroForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils import timezone
from .models import Profile
from .forms import OrdenServicioForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('home')
            else:
                perfil = Profile.objects.get(user=user)
                if perfil.rol == 'asesor':
                    return redirect('pagina_asesor')
                elif perfil.rol == 'mecanico':
                    return redirect('pagina_mecanico')
                elif perfil.rol == 'calidad':
                    return redirect('pagina_calidad')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(
                user=user,
                rol=form.cleaned_data['rol']
            )
            login(request, user)
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'accounts/registro.html', {'form': form})

#Paginas para los roles
def home_view(request):
    return render(request, 'accounts/home.html')

def pagina_asesor_view(request):
    if request.method == 'POST':
        form = OrdenServicioForm(request.POST)
        if form.is_valid():
            orden = form.save(commit=False)
            orden.asesor = request.user
            orden.recepcion_fecha = timezone.now().date()
            orden.recepcion_hora = timezone.now().time()
            orden.save()
            return redirect('pagina_asesor')
    else:
        form = OrdenServicioForm()  
    
    return render(request, 'accounts/pagina_asesor.html', {'form': form})

def pagina_mecanico_view(request):
    return render(request, 'accounts/pagina_mecanico.html')

def pagina_calidad_view(request):
    return render(request, 'accounts/pagina_calidad.html')

def pagina_administracion_view(request):
    return render(request, 'accounts/pagina_administracion.html')

def pagina_bodega_view(request):
    return render(request, 'accounts/pagina_bodega.html')
