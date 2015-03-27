from decimal import Decimal


def calcul_p(request):
    precio = 0
    if request.session['cuenta']:
        for x in request.session['cuenta']:
            precio = precio + (Decimal(x['punitario']) * Decimal(x['cantidad']))
    return precio
