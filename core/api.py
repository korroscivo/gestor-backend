from . import models
from . import serializers
from rest_framework import viewsets, permissions


class ProyectoViewSet(viewsets.ModelViewSet):
    """ViewSet for the Proyecto class"""

    queryset = models.Proyecto.objects.all()
    serializer_class = serializers.ProyectoSerializer
    permission_classes = [permissions.IsAuthenticated]


class ColaboradorViewSet(viewsets.ModelViewSet):
    """ViewSet for the Colaborador class"""

    queryset = models.Colaborador.objects.all()
    serializer_class = serializers.ColaboradorSerializer
    permission_classes = [permissions.IsAuthenticated]


class EspecialidadViewSet(viewsets.ModelViewSet):
    """ViewSet for the Especialidad class"""

    queryset = models.Especialidad.objects.all()
    serializer_class = serializers.EspecialidadSerializer
    permission_classes = [permissions.IsAuthenticated]


class BancoViewSet(viewsets.ModelViewSet):
    """ViewSet for the Banco class"""

    queryset = models.Banco.objects.all()
    serializer_class = serializers.BancoSerializer
    permission_classes = [permissions.IsAuthenticated]


class TerrenoViewSet(viewsets.ModelViewSet):
    """ViewSet for the Terreno class"""

    queryset = models.Terreno.objects.all()
    serializer_class = serializers.TerrenoSerializer
    permission_classes = [permissions.IsAuthenticated]


class TerrenoHospedajeViewSet(viewsets.ModelViewSet):
    """ViewSet for the TerrenoHospedaje class"""

    queryset = models.TerrenoHospedaje.objects.all()
    serializer_class = serializers.TerrenoHospedajeSerializer
    permission_classes = [permissions.IsAuthenticated]


class TerrenoMovilizacionViewSet(viewsets.ModelViewSet):
    """ViewSet for the TerrenoMovilizacion class"""

    queryset = models.TerrenoMovilizacion.objects.all()
    serializer_class = serializers.TerrenoMovilizacionSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProveedorViewSet(viewsets.ModelViewSet):
    """ViewSet for the Proveedor class"""

    queryset = models.Proveedor.objects.all()
    serializer_class = serializers.ProveedorSerializer
    permission_classes = [permissions.IsAuthenticated]


class VueloViewSet(viewsets.ModelViewSet):
    """ViewSet for the Vuelo class"""

    queryset = models.Vuelo.objects.all()
    serializer_class = serializers.VueloSerializer
    permission_classes = [permissions.IsAuthenticated]


class TerrenoDetalleViewSet(viewsets.ModelViewSet):
    """ViewSet for the TerrenoDetalle class"""

    queryset = models.TerrenoDetalle.objects.all()
    serializer_class = serializers.TerrenoDetalleSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProveedorCategoriaViewSet(viewsets.ModelViewSet):
    """ViewSet for the ProveedorCategoria class"""

    queryset = models.ProveedorCategoria.objects.all()
    serializer_class = serializers.ProveedorCategoriaSerializer
    permission_classes = [permissions.IsAuthenticated]


class VehiculoViewSet(viewsets.ModelViewSet):
    """ViewSet for the Vehiculo class"""

    queryset = models.Vehiculo.objects.all()
    serializer_class = serializers.VehiculoSerializer
    permission_classes = [permissions.IsAuthenticated]


class TipoVehiculoViewSet(viewsets.ModelViewSet):
    """ViewSet for the TipoVehiculo class"""

    queryset = models.TipoVehiculo.objects.all()
    serializer_class = serializers.TipoVehiculoSerializer
    permission_classes = [permissions.IsAuthenticated]


class MovimientosContablesViewSet(viewsets.ModelViewSet):
    """ViewSet for the MovimientosContables class"""

    queryset = models.MovimientosContables.objects.all()
    serializer_class = serializers.MovimientosContablesSerializer
    permission_classes = [permissions.IsAuthenticated]


class MedioPagoViewSet(viewsets.ModelViewSet):
    """ViewSet for the MedioPago class"""

    queryset = models.MedioPago.objects.all()
    serializer_class = serializers.MedioPagoSerializer
    permission_classes = [permissions.IsAuthenticated]
