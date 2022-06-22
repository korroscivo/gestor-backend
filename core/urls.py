from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'proyecto', api.ProyectoViewSet)
router.register(r'colaborador', api.ColaboradorViewSet)
router.register(r'especialidad', api.EspecialidadViewSet)
router.register(r'banco', api.BancoViewSet)
router.register(r'terreno', api.TerrenoViewSet)
router.register(r'terrenohospedaje', api.TerrenoHospedajeViewSet)
router.register(r'terrenomovilizacion', api.TerrenoMovilizacionViewSet)
router.register(r'proveedor', api.ProveedorViewSet)
router.register(r'vuelo', api.VueloViewSet)
router.register(r'terrenodetalle', api.TerrenoDetalleViewSet)
router.register(r'proveedorcategoria', api.ProveedorCategoriaViewSet)
router.register(r'vehiculo', api.VehiculoViewSet)
router.register(r'tipovehiculo', api.TipoVehiculoViewSet)
router.register(r'movimientoscontables', api.MovimientosContablesViewSet)
router.register(r'mediopago', api.MedioPagoViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for Proyecto
    path('core/proyecto/', views.ProyectoListView.as_view(), name='core_proyecto_list'),
    path('core/proyecto/create/', views.ProyectoCreateView.as_view(), name='core_proyecto_create'),
    path('core/proyecto/detail/<slug:slug>/', views.ProyectoDetailView.as_view(), name='core_proyecto_detail'),
    path('core/proyecto/update/<slug:slug>/', views.ProyectoUpdateView.as_view(), name='core_proyecto_update'),
)

urlpatterns += (
    # urls for Colaborador
    path('core/colaborador/', views.ColaboradorListView.as_view(), name='core_colaborador_list'),
    path('core/colaborador/create/', views.ColaboradorCreateView.as_view(), name='core_colaborador_create'),
    path('core/colaborador/detail/<slug:slug>/', views.ColaboradorDetailView.as_view(), name='core_colaborador_detail'),
    path('core/colaborador/update/<slug:slug>/', views.ColaboradorUpdateView.as_view(), name='core_colaborador_update'),
)

urlpatterns += (
    # urls for Especialidad
    path('core/especialidad/', views.EspecialidadListView.as_view(), name='core_especialidad_list'),
    path('core/especialidad/create/', views.EspecialidadCreateView.as_view(), name='core_especialidad_create'),
    path('core/especialidad/detail/<slug:slug>/', views.EspecialidadDetailView.as_view(), name='core_especialidad_detail'),
    path('core/especialidad/update/<slug:slug>/', views.EspecialidadUpdateView.as_view(), name='core_especialidad_update'),
)

urlpatterns += (
    # urls for Banco
    path('core/banco/', views.BancoListView.as_view(), name='core_banco_list'),
    path('core/banco/create/', views.BancoCreateView.as_view(), name='core_banco_create'),
    path('core/banco/detail/<slug:slug>/', views.BancoDetailView.as_view(), name='core_banco_detail'),
    path('core/banco/update/<slug:slug>/', views.BancoUpdateView.as_view(), name='core_banco_update'),
)

urlpatterns += (
    # urls for Terreno
    path('core/terreno/', views.TerrenoListView.as_view(), name='core_terreno_list'),
    path('core/terreno/create/', views.TerrenoCreateView.as_view(), name='core_terreno_create'),
    path('core/terreno/detail/<slug:slug>/', views.TerrenoDetailView.as_view(), name='core_terreno_detail'),
    path('core/terreno/update/<slug:slug>/', views.TerrenoUpdateView.as_view(), name='core_terreno_update'),
)

urlpatterns += (
    # urls for TerrenoHospedaje
    path('core/terrenohospedaje/', views.TerrenoHospedajeListView.as_view(), name='core_terrenohospedaje_list'),
    path('core/terrenohospedaje/create/', views.TerrenoHospedajeCreateView.as_view(), name='core_terrenohospedaje_create'),
    path('core/terrenohospedaje/detail/<slug:slug>/', views.TerrenoHospedajeDetailView.as_view(), name='core_terrenohospedaje_detail'),
    path('core/terrenohospedaje/update/<slug:slug>/', views.TerrenoHospedajeUpdateView.as_view(), name='core_terrenohospedaje_update'),
)

urlpatterns += (
    # urls for TerrenoMovilizacion
    path('core/terrenomovilizacion/', views.TerrenoMovilizacionListView.as_view(), name='core_terrenomovilizacion_list'),
    path('core/terrenomovilizacion/create/', views.TerrenoMovilizacionCreateView.as_view(), name='core_terrenomovilizacion_create'),
    path('core/terrenomovilizacion/detail/<int:pk>/', views.TerrenoMovilizacionDetailView.as_view(), name='core_terrenomovilizacion_detail'),
    path('core/terrenomovilizacion/update/<int:pk>/', views.TerrenoMovilizacionUpdateView.as_view(), name='core_terrenomovilizacion_update'),
)

urlpatterns += (
    # urls for Proveedor
    path('core/proveedor/', views.ProveedorListView.as_view(), name='core_proveedor_list'),
    path('core/proveedor/create/', views.ProveedorCreateView.as_view(), name='core_proveedor_create'),
    path('core/proveedor/detail/<slug:slug>/', views.ProveedorDetailView.as_view(), name='core_proveedor_detail'),
    path('core/proveedor/update/<slug:slug>/', views.ProveedorUpdateView.as_view(), name='core_proveedor_update'),
)

urlpatterns += (
    # urls for Vuelo
    path('core/vuelo/', views.VueloListView.as_view(), name='core_vuelo_list'),
    path('core/vuelo/create/', views.VueloCreateView.as_view(), name='core_vuelo_create'),
    path('core/vuelo/detail/<int:pk>/', views.VueloDetailView.as_view(), name='core_vuelo_detail'),
    path('core/vuelo/update/<int:pk>/', views.VueloUpdateView.as_view(), name='core_vuelo_update'),
)

urlpatterns += (
    # urls for TerrenoDetalle
    path('core/terrenodetalle/', views.TerrenoDetalleListView.as_view(), name='core_terrenodetalle_list'),
    path('core/terrenodetalle/create/', views.TerrenoDetalleCreateView.as_view(), name='core_terrenodetalle_create'),
    path('core/terrenodetalle/detail/<int:pk>/', views.TerrenoDetalleDetailView.as_view(), name='core_terrenodetalle_detail'),
    path('core/terrenodetalle/update/<int:pk>/', views.TerrenoDetalleUpdateView.as_view(), name='core_terrenodetalle_update'),
)

urlpatterns += (
    # urls for ProveedorCategoria
    path('core/proveedorcategoria/', views.ProveedorCategoriaListView.as_view(), name='core_proveedorcategoria_list'),
    path('core/proveedorcategoria/create/', views.ProveedorCategoriaCreateView.as_view(), name='core_proveedorcategoria_create'),
    path('core/proveedorcategoria/detail/<slug:slug>/', views.ProveedorCategoriaDetailView.as_view(), name='core_proveedorcategoria_detail'),
    path('core/proveedorcategoria/update/<slug:slug>/', views.ProveedorCategoriaUpdateView.as_view(), name='core_proveedorcategoria_update'),
)

urlpatterns += (
    # urls for Vehiculo
    path('core/vehiculo/', views.VehiculoListView.as_view(), name='core_vehiculo_list'),
    path('core/vehiculo/create/', views.VehiculoCreateView.as_view(), name='core_vehiculo_create'),
    path('core/vehiculo/detail/<int:pk>/', views.VehiculoDetailView.as_view(), name='core_vehiculo_detail'),
    path('core/vehiculo/update/<int:pk>/', views.VehiculoUpdateView.as_view(), name='core_vehiculo_update'),
)

urlpatterns += (
    # urls for TipoVehiculo
    path('core/tipovehiculo/', views.TipoVehiculoListView.as_view(), name='core_tipovehiculo_list'),
    path('core/tipovehiculo/create/', views.TipoVehiculoCreateView.as_view(), name='core_tipovehiculo_create'),
    path('core/tipovehiculo/detail/<slug:slug>/', views.TipoVehiculoDetailView.as_view(), name='core_tipovehiculo_detail'),
    path('core/tipovehiculo/update/<slug:slug>/', views.TipoVehiculoUpdateView.as_view(), name='core_tipovehiculo_update'),
)

urlpatterns += (
    # urls for MovimientosContables
    path('core/movimientoscontables/', views.MovimientosContablesListView.as_view(), name='core_movimientoscontables_list'),
    path('core/movimientoscontables/create/', views.MovimientosContablesCreateView.as_view(), name='core_movimientoscontables_create'),
    path('core/movimientoscontables/detail/<int:pk>/', views.MovimientosContablesDetailView.as_view(), name='core_movimientoscontables_detail'),
    path('core/movimientoscontables/update/<int:pk>/', views.MovimientosContablesUpdateView.as_view(), name='core_movimientoscontables_update'),
)

urlpatterns += (
    # urls for MedioPago
    path('core/mediopago/', views.MedioPagoListView.as_view(), name='core_mediopago_list'),
    path('core/mediopago/create/', views.MedioPagoCreateView.as_view(), name='core_mediopago_create'),
    path('core/mediopago/detail/<slug:slug>/', views.MedioPagoDetailView.as_view(), name='core_mediopago_detail'),
    path('core/mediopago/update/<slug:slug>/', views.MedioPagoUpdateView.as_view(), name='core_mediopago_update'),
)
