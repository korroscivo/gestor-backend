from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Proyecto, Colaborador, Especialidad, Banco, Terreno, TerrenoHospedaje, TerrenoMovilizacion, Proveedor, Vuelo, TerrenoDetalle, ProveedorCategoria, Vehiculo, TipoVehiculo, MovimientosContables, MedioPago
from .forms import ProyectoForm, ColaboradorForm, EspecialidadForm, BancoForm, TerrenoForm, TerrenoHospedajeForm, TerrenoMovilizacionForm, ProveedorForm, VueloForm, TerrenoDetalleForm, ProveedorCategoriaForm, VehiculoForm, TipoVehiculoForm, MovimientosContablesForm, MedioPagoForm


class ProyectoListView(ListView):
    model = Proyecto


class ProyectoCreateView(CreateView):
    model = Proyecto
    form_class = ProyectoForm


class ProyectoDetailView(DetailView):
    model = Proyecto


class ProyectoUpdateView(UpdateView):
    model = Proyecto
    form_class = ProyectoForm


class ColaboradorListView(ListView):
    model = Colaborador


class ColaboradorCreateView(CreateView):
    model = Colaborador
    form_class = ColaboradorForm


class ColaboradorDetailView(DetailView):
    model = Colaborador


class ColaboradorUpdateView(UpdateView):
    model = Colaborador
    form_class = ColaboradorForm


class EspecialidadListView(ListView):
    model = Especialidad


class EspecialidadCreateView(CreateView):
    model = Especialidad
    form_class = EspecialidadForm


class EspecialidadDetailView(DetailView):
    model = Especialidad


class EspecialidadUpdateView(UpdateView):
    model = Especialidad
    form_class = EspecialidadForm


class BancoListView(ListView):
    model = Banco


class BancoCreateView(CreateView):
    model = Banco
    form_class = BancoForm


class BancoDetailView(DetailView):
    model = Banco


class BancoUpdateView(UpdateView):
    model = Banco
    form_class = BancoForm


class TerrenoListView(ListView):
    model = Terreno


class TerrenoCreateView(CreateView):
    model = Terreno
    form_class = TerrenoForm


class TerrenoDetailView(DetailView):
    model = Terreno


class TerrenoUpdateView(UpdateView):
    model = Terreno
    form_class = TerrenoForm


class TerrenoHospedajeListView(ListView):
    model = TerrenoHospedaje


class TerrenoHospedajeCreateView(CreateView):
    model = TerrenoHospedaje
    form_class = TerrenoHospedajeForm


class TerrenoHospedajeDetailView(DetailView):
    model = TerrenoHospedaje


class TerrenoHospedajeUpdateView(UpdateView):
    model = TerrenoHospedaje
    form_class = TerrenoHospedajeForm


class TerrenoMovilizacionListView(ListView):
    model = TerrenoMovilizacion


class TerrenoMovilizacionCreateView(CreateView):
    model = TerrenoMovilizacion
    form_class = TerrenoMovilizacionForm


class TerrenoMovilizacionDetailView(DetailView):
    model = TerrenoMovilizacion


class TerrenoMovilizacionUpdateView(UpdateView):
    model = TerrenoMovilizacion
    form_class = TerrenoMovilizacionForm


class ProveedorListView(ListView):
    model = Proveedor


class ProveedorCreateView(CreateView):
    model = Proveedor
    form_class = ProveedorForm


class ProveedorDetailView(DetailView):
    model = Proveedor


class ProveedorUpdateView(UpdateView):
    model = Proveedor
    form_class = ProveedorForm


class VueloListView(ListView):
    model = Vuelo


class VueloCreateView(CreateView):
    model = Vuelo
    form_class = VueloForm


class VueloDetailView(DetailView):
    model = Vuelo


class VueloUpdateView(UpdateView):
    model = Vuelo
    form_class = VueloForm


class TerrenoDetalleListView(ListView):
    model = TerrenoDetalle


class TerrenoDetalleCreateView(CreateView):
    model = TerrenoDetalle
    form_class = TerrenoDetalleForm


class TerrenoDetalleDetailView(DetailView):
    model = TerrenoDetalle


class TerrenoDetalleUpdateView(UpdateView):
    model = TerrenoDetalle
    form_class = TerrenoDetalleForm


class ProveedorCategoriaListView(ListView):
    model = ProveedorCategoria


class ProveedorCategoriaCreateView(CreateView):
    model = ProveedorCategoria
    form_class = ProveedorCategoriaForm


class ProveedorCategoriaDetailView(DetailView):
    model = ProveedorCategoria


class ProveedorCategoriaUpdateView(UpdateView):
    model = ProveedorCategoria
    form_class = ProveedorCategoriaForm


class VehiculoListView(ListView):
    model = Vehiculo


class VehiculoCreateView(CreateView):
    model = Vehiculo
    form_class = VehiculoForm


class VehiculoDetailView(DetailView):
    model = Vehiculo


class VehiculoUpdateView(UpdateView):
    model = Vehiculo
    form_class = VehiculoForm


class TipoVehiculoListView(ListView):
    model = TipoVehiculo


class TipoVehiculoCreateView(CreateView):
    model = TipoVehiculo
    form_class = TipoVehiculoForm


class TipoVehiculoDetailView(DetailView):
    model = TipoVehiculo


class TipoVehiculoUpdateView(UpdateView):
    model = TipoVehiculo
    form_class = TipoVehiculoForm


class MovimientosContablesListView(ListView):
    model = MovimientosContables


class MovimientosContablesCreateView(CreateView):
    model = MovimientosContables
    form_class = MovimientosContablesForm


class MovimientosContablesDetailView(DetailView):
    model = MovimientosContables


class MovimientosContablesUpdateView(UpdateView):
    model = MovimientosContables
    form_class = MovimientosContablesForm


class MedioPagoListView(ListView):
    model = MedioPago


class MedioPagoCreateView(CreateView):
    model = MedioPago
    form_class = MedioPagoForm


class MedioPagoDetailView(DetailView):
    model = MedioPago


class MedioPagoUpdateView(UpdateView):
    model = MedioPago
    form_class = MedioPagoForm