from django.shortcuts import render

def index(request):
    normas = [
        {"sigla": "RNE", "descripcion": "Reglamento Nacional de Edificaciones (resúmenes)"},
        {"sigla": "MTC", "descripcion": "Manual de carreteras (resúmenes)"},
        {"sigla": "ANA", "descripcion": "Guías y metodología de hidrología (resúmenes)"},
    ]
    return render(request, "resources/index.html", {"normas": normas})
