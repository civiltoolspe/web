from django.shortcuts import render

def index(request):
    posts = [
        {"titulo": "Cómo calcular un hidrograma en 5 pasos", "fecha": "2025-08-31"},
        {"titulo": "Errores comunes al usar curvas IDF", "fecha": "2025-08-20"},
        {"titulo": "Peraltes en curvas: guía rápida", "fecha": "2025-08-10"},
    ]
    return render(request, "blog/index.html", {"posts": posts})
