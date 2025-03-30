from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro_view, name='registro'),
    path('home/', views.home_view, name='home'),
    path('asesor/nueva-orden', views.pagina_asesor_view, name='pagina_asesor'),
    path('pagina-mecanico/', views.pagina_mecanico_view, name='pagina_mecanico'),
    path('pagina-calidad/', views.pagina_calidad_view, name='pagina_calidad'),
    path('pagina-administracion/', views.pagina_administracion_view, name='pagina_administracion'),
    path('pagina-bodega', views.pagina_bodega_view, name='pagina_bodega'),
]