from django.contrib import admin
from django.urls import path, include
from Usuarios.views import rota_protegida
""

urlpatterns = [
    path('admin/' , admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('rota-protegida/', rota_protegida, name='rota-protegida'),
    
]