from django.conf.urls import patterns, include, url
from django.contrib import admin



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PuntoVenta.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('Apps.Ventas.urls', namespace='Venta')),
    url(r'^', include('Apps.Producto.urls', namespace='Producto')),
    url(r'^admin/', include(admin.site.urls)),
)
