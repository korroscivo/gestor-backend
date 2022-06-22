from . import models

from rest_framework import serializers


class ProyectoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Proyecto
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'codigo', 
            'activo', 
        )


class ColaboradorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Colaborador
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'apellido', 
            'rut', 
            'fecha_nacimiento', 
            'direccion', 
            'comuna', 
            'telefono', 
            'email', 
            'cuenta_banco', 
            'tipo_cuenta_banco', 
            'activo', 
        )


class EspecialidadSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Especialidad
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
        )


class BancoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Banco
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
        )


class TerrenoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Terreno
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'fecha_desde', 
            'fecha_hasta', 
            'dias_duracion', 
            'region', 
            'comuna', 
            'activo', 
        )


class TerrenoHospedajeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TerrenoHospedaje
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'fecha_desde', 
            'fecha_hasta', 
            'monto', 
        )


class TerrenoMovilizacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TerrenoMovilizacion
        fields = (
            'pk', 
            'created', 
            'last_updated', 
            'fecha_desde', 
            'fecha_hasta', 
            'cantidad', 
            'monto', 
        )


class ProveedorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Proveedor
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'rut', 
            'contacto_nombre', 
            'contacto_rut', 
            'contacto_telefono', 
            'contacto_email', 
            'direccion', 
            'banco_cuenta', 
            'banco_tipo_cuenta', 
            'activo', 
            'comuna', 
        )


class VueloSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Vuelo
        fields = (
            'pk', 
            'created', 
            'last_updated', 
            'fecha_vuelo', 
            'numero_vuelo', 
            'documento_adjunto_1', 
            'monto', 
            'documento_adjunto_2', 
            'documento_adjunto_3', 
        )


class TerrenoDetalleSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TerrenoDetalle
        fields = (
            'pk', 
            'created', 
            'last_updated', 
            'monto_diario', 
            'cantidad_dias', 
        )


class ProveedorCategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProveedorCategoria
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
        )


class VehiculoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Vehiculo
        fields = (
            'pk', 
            'created', 
            'last_updated', 
            'numero_reserva', 
        )


class TipoVehiculoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TipoVehiculo
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
        )


class MovimientosContablesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MovimientosContables
        fields = (
            'pk', 
            'created', 
            'last_updated', 
            'monto', 
            'activo', 
            'tipo_movimiento', 
            'tabla', 
            'pk_referencia', 
        )


class MedioPagoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MedioPago
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
        )