from django.shortcuts import render

def index(request):
    microcursos = [
        {"titulo": "Manning en canales (1 h)", "link": "#"},
        {"titulo": "Curvas IDF en Excel (1 h)", "link": "#"},
        {"titulo": "Automatización con Python (2 h)", "link": "#"},
    ]
    return render(request, "courses/index.html", {"microcursos": microcursos})
