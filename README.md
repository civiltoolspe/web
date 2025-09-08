# CIVIL TOOLS HUB – PROYECTO DJANGO

Proyecto base para una plataforma con calculadoras, plantillas, microcursos y blog para ingeniería civil.

## Requisitos
- Python 3.10+
- pip
- (Opcional) virtualenv

## Instalación rápida
```bash
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver
```

Accede a http://127.0.0.1:8000/

## Estructura de apps
- core: página de inicio, layout base, estáticos.
- calculators: vistas y endpoints de calculadoras online.
- templates_store: listado/descarga de plantillas (Excel/Python/AutoCAD).
- courses: microcursos gratuitos y cursos avanzados (placeholder).
- blog: artículos técnicos.
- resources: resúmenes de normas y guías.
- community: foro/casos prácticos (placeholder).

