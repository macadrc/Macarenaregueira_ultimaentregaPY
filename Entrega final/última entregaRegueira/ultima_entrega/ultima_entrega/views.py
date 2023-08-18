from django.shortcuts import render, redirect
from .forms import RecetaForm, UsuarioForm, BusquedaForm
from .models import Recetas
from django.shortcuts import render, get_object_or_404, redirect
from .models import Articulo
from .forms import ArticuloForm


def crear_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_articulos')
    else:
        form = ArticuloForm()
    return render(request, 'crear_articulo.html', {'form': form})

def editar_articulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES, instance=articulo)
        if form.is_valid():
            form.save()
            return redirect('lista_articulos')
    else:
        form = ArticuloForm(instance=articulo)
    return render(request, 'editar_articulo.html', {'form': form})

def eliminar_articulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    if request.method == 'POST':
        articulo.delete()
        return redirect('lista_articulos')
    return render(request, 'eliminar_articulo.html', {'articulo': articulo})

def index(request):
    return render(request, 'index.html')

def insertar_datos(request):
    if request.method == 'POST':
        receta_form = RecetaForm(request.POST)
        usuario_form = UsuarioForm(request.POST)
        if receta_form.is_valid() and usuario_form.is_valid():
            receta_form.save()
            usuario_form.save()
            return redirect('index')  
    else:
        receta_form = RecetaForm()
        usuario_form = UsuarioForm()
    return render(request, 'insertar_datos.html', {'receta_form': receta_form, 'usuario_form': usuario_form})

def buscar(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            termino_busqueda = form.cleaned_data.get('termino_busqueda')
            resultados = Recetas.objects.filter(nombre__icontains=termino_busqueda)
            return render(request, 'resultados_busqueda.html', {'resultados': resultados})
    else:
        form = BusquedaForm()
    return render(request, 'buscar.html', {'form': form})



