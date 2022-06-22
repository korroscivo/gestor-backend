from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import CharField
from django.db.models import DateField
from django.db.models import DateTimeField
from django.db.models import EmailField
from django.db.models import IntegerField
from django.db.models import TextField
from django_extensions.db.fields import AutoSlugField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields
from django.contrib import admin
from django.utils.html import format_html




class Proyecto(models.Model):

    # Fields
    name = models.CharField(max_length=255, verbose_name="Nombre")
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    codigo = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)


    # Relationship Fields

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('core_proyecto_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('core_proyecto_update', args=(self.slug,))

    def __str__(self):
        return self.name

class Colaborador(models.Model):

    # Fields
    name = models.CharField(max_length=255, verbose_name="Nombre")
    slug = extension_fields.AutoSlugField(populate_from='rut', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    apellido = models.CharField(max_length=100)
    rut = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    direccion = models.CharField(max_length=100, blank=True)
    comuna = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=12, blank=True)
    email = models.EmailField(blank=True)
    cuenta_banco = models.CharField(max_length=20, blank=True)
    tipo_cuenta_banco = models.CharField(max_length=20, blank=True)
    activo = models.BooleanField(default=True)

    # Relationship Fields
    especialidads = models.ForeignKey(
        'core.Especialidad',
        on_delete=models.CASCADE, related_name="colaboradors", blank=True,
        null=True,
    )
    banco = models.ForeignKey(
        'core.Banco',
        on_delete=models.CASCADE, related_name="colaboradors", blank=True,
        null=True,
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('core_colaborador_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('core_colaborador_update', args=(self.slug,))

    def __str__(self):
        return self.name + ' ' + self.apellido


class Especialidad(models.Model):

    # Fields
    name = models.CharField(max_length=255, verbose_name="Nombre")
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('core_especialidad_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('core_especialidad_update', args=(self.slug,))

    def __str__(self):
        return self.name


class Banco(models.Model):

    # Fields
    name = models.CharField(max_length=255, verbose_name="Nombre")
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('core_banco_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('core_banco_update', args=(self.slug,))


class Terreno(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    fecha_desde = models.DateField()
    fecha_hasta = models.DateField()
    dias_duracion = models.IntegerField()
    region = models.CharField(max_length=30)
    comuna = models.CharField(max_length=30)
    activo = models.BooleanField(default=True)

    # Relationship Fields
    # colaboradores = models.ManyToManyField(
    #     'core.Colaborador',
    #     related_name="terrenos", blank=True, 
    # )
    proyecto = models.ForeignKey(
        'core.Proyecto',
        on_delete=models.CASCADE, related_name="terrenos", 
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('core_terreno_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('core_terreno_update', args=(self.slug,))
    
    def __str__(self):
        return self.proyecto.name + ' - ' + self.name


class TerrenoHospedaje(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    fecha_desde = models.DateField()
    fecha_hasta = models.DateField()
    monto = models.IntegerField()

    # Relationship Fields
    proveedor = models.ForeignKey(
        'core.Proveedor',
        on_delete=models.CASCADE, related_name="terrenohospedajes", 
    )
    terreno = models.ForeignKey(
        'core.Terreno',
        on_delete=models.CASCADE, related_name="terrenohospedajes",
        blank=True, null=True,
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('core_terrenohospedaje_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('core_terrenohospedaje_update', args=(self.slug,))


class TerrenoMovilizacion(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    fecha_desde = models.DateField()
    fecha_hasta = models.DateField()
    cantidad = models.IntegerField()
    monto = models.IntegerField(null=True, blank=True)

    # Relationship Fields
    proveedor = models.ForeignKey(
        'core.Proveedor',
        on_delete=models.CASCADE, related_name="terrenomovilizacions", 
    )
    terreno = models.ForeignKey(
        'core.Terreno',
        on_delete=models.CASCADE, related_name="terrenomovilizacions", 
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('core_terrenomovilizacion_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('core_terrenomovilizacion_update', args=(self.pk,))


class Proveedor(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    rut = models.TextField(max_length=100, null=True, blank=True)
    contacto_nombre = models.TextField(max_length=100, null=True, blank=True)
    contacto_rut = models.TextField(max_length=100, null=True, blank=True)
    contacto_telefono = models.TextField(max_length=100, null=True, blank=True)
    contacto_email = models.TextField(max_length=100, null=True, blank=True)
    direccion = models.TextField(max_length=100, null=True, blank=True)
    banco_cuenta = models.TextField(max_length=100, null=True, blank=True)
    banco_tipo_cuenta = models.CharField(
        max_length=16,
        choices=(
            ('', ''),
            ('Cuenta Corriente', 'Cuenta Corriente'),
            ('Cuenta Vista', 'Cuenta Vista'),
        ),
        default='' , null=True, blank=True)
    activo = models.BooleanField(default=True)
    comuna = models.CharField(max_length=25, null=True, blank=True)

    # Relationship Fields
    banco = models.ForeignKey(
        'core.Banco',
        on_delete=models.CASCADE, related_name="proveedors", null=True, blank=True,
    )
    categoria = models.ForeignKey(
        'core.ProveedorCategoria',
        on_delete=models.CASCADE, related_name="proveedors", null=True, blank=True,
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('core_proveedor_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('core_proveedor_update', args=(self.slug,))

    def __str__(self):
        return self.name
    

def vuelo_path_1(instance, filename):
    return  'logistica/proyectos/{0}/{1}_{2}/vuelos/{3}_1_{4}'.format(instance.terreno.proyecto.slug, instance.terreno.id, instance.terreno.slug, \
        instance.id, filename)
def vuelo_path_2(instance, filename):
    return 'logistica/proyectos/{0}/{1}_{2}/vuelos/{3}_1_{4}'.format(instance.terreno.proyecto.slug, instance.terreno.id, instance.terreno.slug, \
        instance.id, filename)
def vuelo_path_3(instance, filename):
    return 'logistica/proyectos/{0}/{1}_{2}/vuelos/{3}_1_{4}'.format(instance.terreno.proyecto.slug, instance.terreno.id, instance.terreno.slug, \
        instance.id, filename)


class TerrenoDetalle(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    monto_diario = models.IntegerField(null=True)
    cantidad_dias = models.IntegerField(null=True)

    # Relationship Fields
    terreno = models.ForeignKey(
        'core.Terreno',
        on_delete=models.CASCADE, related_name="terrenodetalles", 
    )
    colaborador = models.ForeignKey(
        'core.Colaborador',
        on_delete=models.CASCADE, related_name="terrenodetalles", 
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('core_terrenodetalle_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('core_terrenodetalle_update', args=(self.pk,))

    def __str__(self):
        return self.colaborador.name


class Vuelo(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    fecha_vuelo = models.DateTimeField()
    numero_vuelo = models.CharField(max_length=30, null=True, blank=True)
    monto = models.IntegerField(null=True, blank=True)
    documento_adjunto_1 = models.FileField(upload_to=vuelo_path_1, null=True, blank=True)
    documento_adjunto_2 = models.FileField(upload_to=vuelo_path_2, null=True, blank=True)
    documento_adjunto_3 = models.FileField(upload_to=vuelo_path_3, null=True, blank=True)

    # Relationship Fields
    proveedor = models.ForeignKey(
        'core.Proveedor',
        on_delete=models.CASCADE, related_name="vuelos",  null=True, blank=True
    )
    colaborador = models.ForeignKey(
        'core.Colaborador',
        on_delete=models.CASCADE, related_name="vuelos"
    )
    terreno = models.ForeignKey(
        'core.Terreno',
        on_delete=models.CASCADE, related_name="vuelos", blank=True,
        null=True,
    )
    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('core_vuelo_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('core_vuelo_update', args=(self.pk,))

    def __str__(self):
        return self.terreno.name + ' - ' + self.colaborador.name

    # def colored_name(self):
    #     return format_html(
    #         '<span style="color: #548850;">{}</span>',
    #         self.colaborador
    #     )



class ProveedorCategoria(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('core_proveedorcategoria_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('core_proveedorcategoria_update', args=(self.slug,))

    def __str__(self):
        return self.name


class Vehiculo(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    numero_reserva = models.CharField(max_length=10)

    # Relationship Fields
    tipo_vehiculo = models.ForeignKey(
        'core.TipoVehiculo',
        on_delete=models.CASCADE, related_name="vehiculos", 
    )
    conductor = models.ForeignKey(
        'core.Colaborador',
        on_delete=models.CASCADE, related_name="vehiculos", 
    )
    terreno_movilizacion = models.ForeignKey(
        'core.TerrenoMovilizacion',
        on_delete=models.CASCADE, related_name="vehiculos", 
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('core_vehiculo_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('core_vehiculo_update', args=(self.pk,))


class TipoVehiculo(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('core_tipovehiculo_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('core_tipovehiculo_update', args=(self.slug,))

    def __str__(self):
        return self.name


class MovimientosContables(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    monto = models.IntegerField()
    activo = models.BooleanField(default=True)
    tipo_movimiento = models.CharField(max_length=16,
        choices=(
            ('I', 'Ingreso'),
            ('E', 'Egreso'),
        ),
        default='E')
    tabla = models.CharField(max_length=30)
    pk_referencia = models.IntegerField()

    # Relationship Fields
    medio_pago = models.ForeignKey(
        'core.MedioPago',
        on_delete=models.CASCADE, related_name="movimientoscontabless", 
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('core_movimientoscontables_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('core_movimientoscontables_update', args=(self.pk,))


class MedioPago(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('core_mediopago_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('core_mediopago_update', args=(self.slug,))

    def __str__(self):
        return self.name
    