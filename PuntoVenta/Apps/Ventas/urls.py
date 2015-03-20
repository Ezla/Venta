from django.conf.urls import patterns, url


from .views import Login, Logout, Venta, Venta_Buscar_Producto, Venta_Calcula_Precio, Venta_Remover_Prod, Venta_Cancelar_Cuenta, Venta_Aumentar_Prod

urlpatterns = patterns('',
    url(r'^$', Login.as_view(), name='url_index'),
    url(r'^Logout/$', Logout.as_view(), name='url_logout'),
    url(r'^Venta/$', Venta.as_view(), name='url_venta'),
    url(r'^Ajax/Buscar/$', Venta_Buscar_Producto.as_view(), name="url_buscar_ajax"),
    url(r'^Ajax/Calular/$', Venta_Calcula_Precio.as_view(), name='url_calcula_precio_ajax'),
    url(r'^Ajax/Remover/$', Venta_Remover_Prod.as_view(), name='url_remover_prod_ajax'),
    url(r'^Ajax/Aumentar/$', Venta_Aumentar_Prod.as_view(), name='url_aumentar_prod_ajax'),
    url(r'^Ajax/Cancelar/$', Venta_Cancelar_Cuenta.as_view(), name='url_cancelar_cuenta_ajax'),
)
