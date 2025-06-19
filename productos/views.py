from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .models import Producto
# Create your views here.


def index(request):
    return HttpResponse("PRODUCTOS")


def lista_productos(request):
    productos = Producto.objects.all()

    # return JsonResponse(list(productos), safe=False)
    return render(request, 'lista_productos.html', {'productos': productos})
