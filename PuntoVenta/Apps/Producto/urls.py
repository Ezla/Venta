from django.conf.urls import patterns, url

from .views import Producto_Nuevo, Producto_Lista, Producto_Actualizar, Producto_Eliminar, Producto_Consultar


urlpatterns = patterns('',
    url(r'^Producto/Nuevo/$', Producto_Nuevo.as_view(), name="url_nuevo"),
    url(r'^Producto/Lista/(?P<pk>\d+)/$', Producto_Lista.as_view(), name="url_lista"),
    url(r'^Producto/Actualizar/(?P<pk>\d+)/$', Producto_Actualizar.as_view(), name='url_actualizar'),
    url(r'^Producto/Eliminar/(?P<pk>\d+)/$', Producto_Eliminar.as_view(), name='url_eliminar'), 
    url(r'^Producto/Consultar/(?P<pk>\d+)/$', Producto_Consultar.as_view(), name='url_consultar'),
)
