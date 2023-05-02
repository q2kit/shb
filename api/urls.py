from django.urls import path

from api.views import search, import_excel, contact, export_excel

urlpatterns = [
    path('search/', search, name='search'),
    path('import/', import_excel, name='import'),
    path('contact/', contact, name='contact'),
    path('export/', export_excel, name='export'),
]
