from django.shortcuts import render
from django.http import HttpRequest

def index(request: HttpRequest):
    return render(request, "calculators/index.html")

def canal_rectangular(request: HttpRequest):
    resultado = None
    if request.method == "POST":
        try:
            n = float(request.POST.get("n"))
            S = float(request.POST.get("S"))
            b = float(request.POST.get("b"))
            y = float(request.POST.get("y"))
            # Fórmula de Manning para canal rectangular: Q = (1/n) * A * R^(2/3) * S^(1/2)
            A = b * y
            P = b + 2*y
            R = A / P if P != 0 else 0.0
            Q = (1.0/n) * A * (R**(2.0/3.0)) * (S**0.5)
            resultado = { "A": A, "P": P, "R": R, "Q": Q }
        except Exception as e:
            resultado = { "error": str(e) }
    return render(request, "calculators/canal_rectangular.html", { "resultado": resultado })
