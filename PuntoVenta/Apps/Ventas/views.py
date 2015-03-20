from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView, FormView, View
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import login, logout
from .forms import AuthenticationFormCustom
from Apps.Producto.models import Producto
from decimal import Decimal

class Login(FormView):
    template_name = 'index.html'
    form_class = AuthenticationFormCustom
    success_url =  reverse_lazy('Venta:url_venta')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        self.request.session['cuenta'] = []
        return super(Login, self).form_valid(form)


class Logout(RedirectView):
    url = reverse_lazy('Venta:url_index')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(Logout, self).get(request, *args, **kwargs)


class LoginRequiredMixin(object):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect(reverse_lazy('Venta:url_index'))
        else:
            return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class Venta(LoginRequiredMixin, TemplateView):
    template_name = 'Venta/index.html'

    def dispatch(self, request, *args, **kwargs):
        print request.session['cuenta']
        return super(Venta, self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(Venta, self).get_context_data(**kwargs)
        context['data'] = self.request.session['cuenta']
        precio = 0
        if self.request.session['cuenta']:
            for x in self.request.session['cuenta']:
                precio = precio + (float(x['punitario']) * int(x['cantidad']))
        context['precio'] = precio
        return context


class Venta_Buscar_Producto(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        codigo = request.GET['cod']
            # Agregar - Listado de la compra
        cont = False
        try:
            prod = Producto.objects.get(codigo=codigo)
            if request.session['cuenta']:
                for x in request.session['cuenta']:
                    if x['codigo'] == prod.codigo:
                        x['cantidad'] = str(int(x['cantidad']) + 1)
                        cont = True
                        break
                if cont == False:
                    request.session['cuenta'].append({'codigo': prod.codigo, 'descripcion': prod.descripcion, 'punitario':str(prod.punitario), 'pmayoreo':str(prod.pmayoreo), 'cantidad':str(1)})
            else:
                request.session['cuenta'].append({'codigo': prod.codigo, 'descripcion': prod.descripcion, 'punitario':str(prod.punitario), 'pmayoreo':str(prod.pmayoreo), 'cantidad':str(1)})

            data = JsonResponse(request.session['cuenta'], safe=False)
        except Exception:
            #data = JsonResponse({'descripcion': 'No se encontro el producto'})
            data = JsonResponse(request.session['cuenta'], safe=False)

        print request.session['cuenta']
        request.session.save()
        return HttpResponse(data, content_type='application/json')


class Venta_Remover_Prod(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        codigo = request.GET['cod']
        if request.session['cuenta']:
            for x in request.session['cuenta']:
                if x['codigo'] == codigo:
                    x['cantidad'] = str(int(x['cantidad']) - 1)
                    if int(x['cantidad']) <= 0:
                        request.session['cuenta'].remove(x)
                    break
        request.session.save()
        data = JsonResponse(request.session['cuenta'], safe=False)
        return HttpResponse(data, content_type='application/json')


class Venta_Aumentar_Prod(View):

    def get(self, request, *args, **kwargs):
        codigo = request.GET['cod']
        if request.session['cuenta']:
            for x in request.session['cuenta']:
                if x['codigo'] == codigo:
                    x['cantidad'] = str(int(x['cantidad']) + 1)
                    break
        request.session.save()
        data = JsonResponse(request.session['cuenta'], safe=False)
        return HttpResponse(data, 'application/json')


class Venta_Calcula_Precio(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        precio = 0
        if request.session['cuenta']:
            for x in request.session['cuenta']:
                precio = precio + (Decimal(x['punitario']) * Decimal(x['cantidad']))
        data = JsonResponse({'precio': precio})
        return HttpResponse(data, content_type='application/json')


class Venta_Cancelar_Cuenta(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        request.session['cuenta'] = []
        request.session.save()
        data = JsonResponse({'listo': 'Se a cancelado la cuenta.'})
        return HttpResponse(data, content_type='application/json')