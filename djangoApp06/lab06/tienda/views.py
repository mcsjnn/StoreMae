from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Producto, Categoria
from django.conf import settings

# Create your views here.
def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    categorias = Categoria.objects.all()
    context = {'product_list': product_list, 'categorias': categorias, 'MEDIA_URL': settings.MEDIA_URL}
    return render(request, 'index.html', context)

def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    categorias = Categoria.objects.all()
    context = {'producto': producto, 'categorias': categorias}
    return render(request, 'producto.html', context)

def productos_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    productos = Producto.objects.filter(categoria=categoria)
    categorias = Categoria.objects.all()
    context = {'productos': productos, 'categoria': categoria, 'categorias': categorias}
    return render(request, 'productos_por_categoria.html', context)


