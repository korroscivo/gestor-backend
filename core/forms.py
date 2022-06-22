from django import forms
from .models import Proyecto, Colaborador, Especialidad, Banco, Terreno, TerrenoHospedaje, TerrenoMovilizacion, Proveedor, Vuelo, TerrenoDetalle, ProveedorCategoria, Vehiculo, TipoVehiculo, MovimientosContables, MedioPago


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['name', 'codigo', 'activo']


class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ['name', 'apellido', 'rut', 'fecha_nacimiento', 'direccion', 'comuna', 'telefono', 'email', 'cuenta_banco', 'tipo_cuenta_banco', 'activo', 'especialidads', 'banco']


class EspecialidadForm(forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = ['name']


class BancoForm(forms.ModelForm):
    class Meta:
        model = Banco
        fields = ['name']


class TerrenoForm(forms.ModelForm):
    class Meta:
        model = Terreno
        fields = ['name', 'fecha_desde', 'fecha_hasta', 'dias_duracion', 'region', 'comuna', 'activo', 'proyecto']


class TerrenoHospedajeForm(forms.ModelForm):
    class Meta:
        model = TerrenoHospedaje
        fields = ['name', 'fecha_desde', 'fecha_hasta', 'monto', 'proveedor', 'terreno']


class TerrenoMovilizacionForm(forms.ModelForm):
    class Meta:
        model = TerrenoMovilizacion
        fields = ['fecha_desde', 'fecha_hasta', 'cantidad', 'monto', 'proveedor', 'terreno']


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['name', 'rut', 'contacto_nombre', 'contacto_rut', 'contacto_telefono', 'contacto_email', 'direccion', 'banco_cuenta', 'banco_tipo_cuenta', 'activo', 'comuna', 'banco', 'categoria']


class VueloForm(forms.ModelForm):
    class Meta:
        model = Vuelo
        fields = ['fecha_vuelo', 'numero_vuelo', 'documento_adjunto_1', 'monto', 'documento_adjunto_2', 'documento_adjunto_3', 'proveedor', 'colaborador', 'terreno']


class TerrenoDetalleForm(forms.ModelForm):
    class Meta:
        model = TerrenoDetalle
        fields = ['monto_diario', 'cantidad_dias', 'terreno', 'colaborador']


class ProveedorCategoriaForm(forms.ModelForm):
    class Meta:
        model = ProveedorCategoria
        fields = ['name']


class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['numero_reserva', 'tipo_vehiculo', 'conductor', 'terreno_movilizacion']


class TipoVehiculoForm(forms.ModelForm):
    class Meta:
        model = TipoVehiculo
        fields = ['name']


class MovimientosContablesForm(forms.ModelForm):
    class Meta:
        model = MovimientosContables
        fields = ['monto', 'activo', 'tipo_movimiento', 'tabla', 'pk_referencia', 'medio_pago']


class MedioPagoForm(forms.ModelForm):
    class Meta:
        model = MedioPago
        fields = ['name']