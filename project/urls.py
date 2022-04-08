"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from project.views import bienvenida, home
from project.views import categoriaEdad, obtenerMomentoActual
from project.views import contenidoHTML
from project.views import plantillaExterna1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('bienvenida/', bienvenida),
    path('categoriaEdad/<int:edad>', categoriaEdad),
    path('obtenerMomentoActual/', obtenerMomentoActual),
    path('contenidoHTML/<nombre>/<int:edad>', contenidoHTML),
    path('plantillaExterna1/', plantillaExterna1)
]
