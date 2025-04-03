from django.shortcuts import render, redirect
from django.utils import timezone
from ordenes.forms import OrdenServicioForm

def home_view(request):
    return render(request, 'taller/home.html')

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
    
    return render(request, 'taller/pagina_asesor.html', {'form': form})

def pagina_mecanico_view(request):
    return render(request, 'taller/pagina_mecanico.html')

def pagina_calidad_view(request):
    return render(request, 'taller/pagina_calidad.html')

def pagina_administracion_view(request):
    return render(request, 'taller/pagina_administracion.html')

def pagina_bodega_view(request):
    return render(request, 'taller/pagina_bodega.html')
