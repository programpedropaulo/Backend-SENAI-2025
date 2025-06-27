from django.contrib import admin
from django.urls import path
from Usuarios.views import UsuarioAPIViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', UsuarioAPIViews.as_view()),  # GET e POST
]
