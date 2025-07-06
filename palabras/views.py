from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Palabra

def index(request):
    ultima = None

    if request.method == 'POST':
        texto_ingresado = request.POST.get('texto', '').strip()
        if texto_ingresado:
            Palabra.objects.create(texto=texto_ingresado)
            return redirect('index')  # Redirige después del POST

    if Palabra.objects.exists():
        ultima = Palabra.objects.latest('id')

    return render(request, 'palabras/index.html', {'ultima': ultima})
