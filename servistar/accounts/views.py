from django.shortcuts import render, redirect
from .forms import RegistroForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Profile

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('taller:home')
            else:
                perfil = Profile.objects.get(user=user)
                if perfil.rol == 'asesor':
                    return redirect('taller:pagina_asesor')
                elif perfil.rol == 'mecanico':
                    return redirect('taller:pagina_mecanico')
                elif perfil.rol == 'calidad':
                    return redirect('taller:pagina_calidad')
                elif perfil.rol == 'administracion':
                    return redirect('taller:pagina_administracion')
                elif perfil.rol == 'bodega':
                    return redirect('taller:pagina_bodega')
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
