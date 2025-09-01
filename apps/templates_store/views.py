from django.shortcuts import render

def index(request):
    # Placeholder de listado; en el futuro, alimentar desde BD
    templates = [
        {"nombre": "Curvas IDF (Excel)", "descripcion": "Plantilla para cálculo de intensidades", "archivo": "#"},
        {"nombre": "Cunetas (Excel)", "descripcion": "Dimensionamiento básico de cunetas", "archivo": "#"},
        {"nombre": "Hidrograma (Python)", "descripcion": "Script para generar hidrograma sintético", "archivo": "#"},
    ]
    return render(request, "templates_store/index.html", {"templates": templates})
