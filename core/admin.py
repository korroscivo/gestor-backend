from django.contrib import admin
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Proyecto, Colaborador, Especialidad, Banco, Terreno, TerrenoHospedaje, TerrenoMovilizacion, Proveedor, Vuelo, TerrenoDetalle, \
ProveedorCategoria, MedioPago, MovimientosContables, TipoVehiculo, Vehiculo
from django.utils.safestring import mark_safe
from django.urls import reverse
import locale

# Cambios en el Dashboear del Admin

admin.site.site_header = "Sistema de Gestion Econsult Group"


######################
###### FORM ##########
######################

# Vuelo
class VueloAdminForm(forms.ModelForm):
    # terrenodetalle = TerrenoDetalle.objects.get(id=self.terrenodetalle.id)
    colaborador = forms.ModelChoiceField(queryset = Colaborador.objects.filter(pk__in= [1,2,3]))#here you can filter for what choices you need
    
    class Meta:
        model = Vuelo
        fields = ['colaborador',
            'terreno',
            'proveedor',
            'fecha_vuelo', 
            'numero_vuelo', 
            'monto',
            'documento_adjunto_1',
            'documento_adjunto_2', 
            'documento_adjunto_3'
        ]
    # def __init__(self, *args, **kwargs):
    #     print(self.numero)

# Terreno
class TerrenoAdminForm(forms.ModelForm):
    # colaboradores = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset = Colaborador.objects.all())#here you can filter for what choices you need
    # colaboradores = forms.ModelMultipleChoiceField(queryset=Colaborador.objects.all(), label="Colaboradores", widget=FilteredSelectMultiple("Colaboradores", is_stacked=False), required=False)
    class Meta:
        model = Terreno
        fields = ['name', 'fecha_desde', 'fecha_hasta', 'dias_duracion', 'region', 'comuna'] 
        # '__all__'

# Terreno Detalle
class TerrenoDetalleForm(forms.ModelForm):
    colaborador = forms.ModelChoiceField(queryset = Colaborador.objects.all())#here you can filter for what choices you need
    class Meta:
        model = TerrenoDetalle
        fields = ['colaborador']

# Proveedor
class ProveedorAdminForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['name', 'rut', 'direccion', 'contacto_nombre', 'contacto_rut', 'contacto_telefono', 'contacto_email', 'banco', 'banco_tipo_cuenta', 'banco_cuenta', 'categoria']

# Proveedor Categoria
class ProveedorCategoriaAdminForm(forms.ModelForm):
    class Meta:
        model = ProveedorCategoria
        fields = '__all__'

# Medio Pago
class MedioPagoAdminForm(forms.ModelForm):

    class Meta:
        model = MedioPago
        fields = '__all__'

# Movimientos Contables
class MovimientosContablesAdminForm(forms.ModelForm):
    class Meta:
        model = MovimientosContables
        fields = '__all__'

# Vehiculo
class VehiculoAdminForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = '__all__'

# Tipo Vehiculo
class TipoVehiculoAdminForm(forms.ModelForm):
    class Meta:
        model = TipoVehiculo
        fields = '__all__'

######################
###### INLINE ########
######################

# Terreno
class TerrenoInline(admin.TabularInline):
    model = Terreno
    readonly_fields = ('editar',)

    def get_extra(self, request, obj=None, **kwargs):
        lista = Terreno.objects.filter(proyecto=obj.pk)
        if lista.count():
            return 0
        else:
            return 1

    def editar(self, obj):
        # return mark_safe('<a href="#">Full edit</a>')
        if obj.id:
            return mark_safe('<a href="/admin/core/terreno/%s/change/">Editar</a>' %  obj.id)
        else:
            return mark_safe('')       
        # return mark_safe('<a href="%s">Full edit</a>' % reverse('admin:edit-item', args=(obj.id,)))

# Terreno Detalle
class TerrenoDetalleInline(admin.TabularInline):
    model = TerrenoDetalle
    form = TerrenoDetalleForm
    fields = ('colaborador','monto_diario', 'cantidad_dias')

    def get_extra(self, request, obj=None, **kwargs):
        lista = TerrenoDetalle.objects.filter(terreno=obj.pk)
        if lista.count():
            return 0
        else:
            return 1

    # def get_queryset(self, request):
    #     colab = Colaborador.objects.filter(id = 5)
    #     return colab

# Vuelo
class VuelosInline(admin.TabularInline):
    model = Vuelo
    fields = ('colaborador',
            'terreno',
            'proveedor',
            'fecha_vuelo', 
            'numero_vuelo', 
            'monto',
            'editar')
    readonly_fields = ('editar',)
    form = VueloAdminForm

    def get_extra(self, request, obj=None, **kwargs):
        vuelos = Vuelo.objects.filter(terreno=obj.pk)
        if vuelos.count():
            return 0
        else:
            return 1

    def editar(self, obj):
        # return mark_safe('<a href="#">Full edit</a>')
        if obj.id:
            return mark_safe('<a href="/admin/core/vuelo/%s/change/">Editar</a>' %  obj.id)
        else:
            return mark_safe('')


######################
###### ADMIN ########
######################

# Proyecto
@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    fields = ('name', 'codigo','activo')
    list_display = ['name', 'codigo', 'activo']
    inlines = (TerrenoInline,)

# Colaborador
@admin.register(Colaborador)
class ClaboradorAdmin(admin.ModelAdmin):
    fields = ('name', 'apellido', 'rut', 'fecha_nacimiento', 'direccion', 'comuna', 'telefono', 'email', 'banco', 'cuenta_banco', 'tipo_cuenta_banco',)
    list_display = ['name', 'apellido', 'rut', 'fecha_nacimiento', 'direccion', 'comuna', 'telefono', 'email', 'banco', 'cuenta_banco', 'tipo_cuenta_banco']

# Especialidad
@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    fields = ('name',)

# Banco
@admin.register(Banco)
class BancoAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name', )
    search_fields = ('name', )
        
# Terreno
@admin.register(Terreno)
class TerrenoAdmin(admin.ModelAdmin):
    # form = TerrenoAdminForm
    list_display = ['name', 'proyecto', 'created', 'last_updated', 'fecha_desde', 'fecha_hasta', 'dias_duracion', 'region', 'comuna']
    readonly_fields = [ 'slug', 'created', 'last_updated', 'proyecto']
    inlines = (TerrenoDetalleInline, VuelosInline)

# Vuelo
@admin.register(Vuelo)
class VueloAdmin(admin.ModelAdmin):
    form = VueloAdminForm
    def monto_pasaje (self, obj):
        if(obj.monto):
            return mark_safe('$ %s' %  '{:,}'.format(obj.monto).replace(",", "."))
        else:
            return 0
    # fields = ('name',)
    list_display = ('colaborador',
            'terreno',
            'proveedor',
            'fecha_vuelo', 
            'numero_vuelo', 
            'monto_pasaje'
             )
    search_fields = ['monto', 'colaborador__name','colaborador__apellido', 'colaborador__rut', 'terreno_name']
    readonly_fields = ['terreno',]
    list_filter = ('terreno__proyecto__name', 'terreno__name')

# Proveedor
@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    form = ProveedorAdminForm
    list_display = ['name',  'rut', 'contacto_nombre', 'contacto_rut', 'contacto_telefono', 'contacto_email', 'direccion', 'banco_tipo_cuenta', 'banco_cuenta', 'categoria', 'created', 'last_updated',]
    # readonly_fields = ['name', 'slug', 'created', 'last_updated', 'rut', 'contacto_nombre', 'contacto_rut', 'contacto_telefono', 'contacto_email', 'direccion', 'banco_cuenta', 'banco_tipo_cuenta']

# Proveedor Categoria
@admin.register(ProveedorCategoria)
class ProveedorCategoriaAdmin(admin.ModelAdmin):
    form = ProveedorCategoriaAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated']

# Medio Pago
@admin.register(MedioPago)
class MedioPagoAdmin(admin.ModelAdmin):
    form = MedioPagoAdminForm
    list_display = ['name', 'created', 'last_updated']
    readonly_fields = [ 'created', 'last_updated']

# Movimientos Contables
@admin.register(MovimientosContables)
class MovimientosContablesAdmin(admin.ModelAdmin):
    form = MovimientosContablesAdminForm
    list_display = ['created', 'last_updated', 'monto', 'activo', 'tipo_movimiento', 'tabla', 'pk_referencia']
    readonly_fields = ['created', 'last_updated']

# Vehiculo
@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    form = VehiculoAdminForm
    list_display = ['created', 'last_updated', 'numero_reserva']
    readonly_fields = ['created', 'last_updated', 'numero_reserva']

# Tipo Vehiculo
@admin.register(TipoVehiculo)
class TipoVehiculoAdmin(admin.ModelAdmin):
    form = TipoVehiculoAdminForm
    list_display = ['name',  'created', 'last_updated']
    readonly_fields = ['created', 'last_updated']


# SECCION LOGISTICA VISTAS

# class CopiaProveedorCategoria(ProveedorCategoria):
#     class Meta:
#         proxy = True

# @admin.register(CopiaProveedorCategoria)
# class CopiaProveedorCategoriaAdmin(ProveedorCategoriaAdmin):
#     def make_inactive(modeladmin, request, queryset):
#         pass
#         # queryset.update(is_active = 0)
#         # messages.success(request, "Selected Record(s) Marked as Absent Successfully !!")

#     admin.site.add_action(make_inactive, "Mark Absent")
