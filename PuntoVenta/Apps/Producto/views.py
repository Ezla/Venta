from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from .models import Producto
from .forms import CrearProductoForm
from Apps.Ventas.views import LoginRequiredMixin


class Producto_Nuevo(LoginRequiredMixin, CreateView):
	model = Producto
	form_class = CrearProductoForm
	success_url = '/Producto/Lista/1/'


class Producto_Lista(LoginRequiredMixin, ListView):
	model = Producto
	paginate_by=50

	def get_context_data(self, **kwargs):
		context = super(Producto_Lista, self).get_context_data(**kwargs)
		context['total_productos'] = Producto.objects.count()
		return context


class Producto_Actualizar(LoginRequiredMixin, UpdateView):
	model = Producto
	form_class = CrearProductoForm
	success_url = '/Producto/Lista/1/'


class Producto_Eliminar(LoginRequiredMixin, DeleteView):
	model = Producto
	success_url = '/Producto/Lista/1/'


class Producto_Consultar(LoginRequiredMixin, DetailView):
	model = Producto