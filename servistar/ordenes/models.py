from django.db import models
from django.contrib.auth.models import User

class OrdenServicio(models.Model):
    ESTADOS = (
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completado', 'Completado'),
    )

    # Datos del Cliente
    cliente_nombre = models.CharField(max_length=100, verbose_name='Nombre')
    cliente_telefono = models.CharField(blank=True, max_length=20, verbose_name='Telefono')
    cliente_celular = models.CharField(blank=True, max_length=8, verbose_name='Celular')
    cliente_email = models.EmailField(blank=True, verbose_name='Email')
    cliente_direccion = models.CharField(blank=True, max_length=30, verbose_name='Dirección')

    # Datos del Vehiculo
    vehiculo_marca = models.CharField(max_length=15, verbose_name='Marca')
    vehiculo_modelo = models.CharField(max_length=15, verbose_name='Modelo')
    vehiculo_tipo = models.CharField(max_length=10, verbose_name='Tipo')
    vehiculo_placa = models.CharField(max_length=10, verbose_name='Placa')
    vehiculo_kilometraje = models.FloatField(verbose_name='Km')
    vehiculo_color = models.CharField(max_length=15, verbose_name='Color')
    vehiculo_chasis = models.CharField(max_length=50, verbose_name='Nº de Chasis')
    vehiculo_motor = models.CharField(blank=True, max_length=20, verbose_name='Nº de Motor')
    vehiculo_proforma = models.CharField(blank=True, max_length=20, verbose_name='Nº de Proforma')

    # Entrega, Fecha y Hora
    recepcion_fecha = models.DateField(verbose_name='Fecha de Recepción')
    recepcion_hora = models.TimeField(verbose_name='Hora de Recepción')
    cliente_lugarEntrega = models.CharField(blank=True, max_length=30, verbose_name='Lugar de Entrega')
    cliente_fechaEntrega = models.DateField(blank=True, verbose_name='Fecha de Entrega')
    cliente_horaEntrega = models.TimeField(blank=True, verbose_name='Hora de Entrega')

    # Revisión Técnica
    cambio_aceite = models.BooleanField(default=False)
    cambio_aceite_notas = models.CharField(max_length=200, blank=True)

    revision_nivelesLiquidos = models.BooleanField(default=False)
    revision_nivelesLiquidos_notas = models.CharField(max_length=200, blank=True)

    lavado = models.BooleanField(default=False)
    lavado_notas = models.CharField(max_length=200, blank=True)

    engrase = models.BooleanField(default=False)
    engrase_notas = models.CharField(max_length=200, blank=True)

    motor = models.BooleanField(default=False)
    motor_notas = models.CharField(max_length=200, blank=True)

    afinado_motor = models.BooleanField(default=False)
    afinado_motor_notas = models.CharField(max_length=200, blank=True)

    revision_frenos = models.BooleanField(default=False)
    revision_frenos_notas = models.CharField(max_length=200, blank=True)

    revision_embrague = models.BooleanField(default=False)
    revision_embrague_notas = models.CharField(max_length=200, blank=True)

    revision_transmision = models.BooleanField(default=False)
    revision_transmision_notas = models.CharField(max_length=200, blank=True)

    revision_diferencial = models.BooleanField(default=False)
    revision_diferencial_notas = models.CharField(max_length=200, blank=True)

    revision_crucetas = models.BooleanField(default=False)
    revision_crucetas_notas = models.CharField(max_length=200, blank=True)

    revision_suspensionDelantera = models.BooleanField(default=False)
    revision_suspensionDelantera_notas = models.CharField(max_length=200, blank=True)

    revision_suspensionTrasera = models.BooleanField(default=False)
    revision_suspensionTrasera_notas = models.CharField(max_length=200, blank=True)

    revision_amortiguadores = models.BooleanField(default=False)
    revision_amortiguadores_notas = models.CharField(max_length=200, blank=True)

    revision_sistemasDireccion = models.BooleanField(default=False)
    revision_sistemasDireccion_notas = models.CharField(max_length=200, blank=True)

    revision_rodamientosRuedas = models.BooleanField(default=False)
    revision_rodamientosRuedas_notas = models.CharField(max_length=200, blank=True)

    revision_sistemaElectrico = models.BooleanField(default=False)
    revision_sistemaElectrico_notas = models.CharField(max_length=200, blank=True)

    alineado = models.BooleanField(default=False)
    alineado_notas = models.CharField(max_length=200, blank=True)

    balanceado = models.BooleanField(default=False)
    balanceado_notas = models.CharField(max_length=200, blank=True)

    rotacion = models.BooleanField(default=False)
    rotacion_notas = models.CharField(max_length=200, blank=True)

    alineado_faroles = models.BooleanField(default=False)
    alineado_faroles_notas = models.CharField(max_length=200, blank=True)

    ajuste_interior = models.BooleanField(default=False)
    ajuste_interior_notas = models.CharField(max_length=200, blank=True)

    ajuste_carroceria = models.BooleanField(default=False)
    ajuste_carroceria_notas = models.CharField(max_length=200, blank=True)

    revision_ruido = models.BooleanField(default=False)
    revision_ruido_notas = models.CharField(max_length=200, blank=True)

    otros = models.BooleanField(default=False)
    otros_notas = models.CharField(max_length=200, blank=True)
    

    # Inventario de Recepcion
    limpiaparabrisas = models.BooleanField(default=False)
    radio = models.BooleanField(default=False)
    toca_cintas = models.BooleanField(default=False)
    gomas_pedales = models.BooleanField(default=False)
    sobrepisos = models.BooleanField(default=False)
    luz_techo_interior = models.BooleanField(default=False)
    perillas_seguros = models.BooleanField(default=False)
    encendedor = models.BooleanField(default=False)
    manivelas_puertas = models.BooleanField(default=False)
    estuche_herramientas = models.BooleanField(default=False)
    espejo_interior = models.BooleanField(default=False)
    vidrios_parabrisas = models.BooleanField(default=False)
    manual_propietario = models.BooleanField(default=False)
    tapas_tanque_agua = models.BooleanField(default=False)
    tapa_radiador = models.BooleanField(default=False)
    biseles_delanteros = models.BooleanField(default=False)
    vidrios_laterales = models.BooleanField(default=False)
    antena = models.BooleanField(default=False)
    biseles_traseros = models.BooleanField(default=False)
    tapa_ruedas_cubos = models.BooleanField(default=False)
    espejos_exteriores = models.BooleanField(default=False)
    emblemas = models.BooleanField(default=False)
    guiñadores_delanteros = models.BooleanField(default=False)
    tapa_tanque_combustible = models.BooleanField(default=False)
    faroles_delanteros = models.BooleanField(default=False)
    guiñadores_laterales = models.BooleanField(default=False)
    vidrio_trasero = models.BooleanField(default=False)
    linterna = models.BooleanField(default=False)
    gato = models.BooleanField(default=False)
    palanqueta = models.BooleanField(default=False)
    limpia_parabrisas_trasero = models.BooleanField(default=False)
    llanta_auxilio = models.BooleanField(default=False)
    funda_llanta_auxilio = models.BooleanField(default=False)
    faros_stops = models.BooleanField(default=False)
    vidrios_trasero = models.BooleanField(default=False)

    # Observaciones
    observaciones = models.TextField(blank=True, verbose_name='')
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    asesor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Orden #{self.id} - {self.cliente_nombre}"
