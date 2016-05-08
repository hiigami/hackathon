"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', Home.as_view()),
    url(r'^contratar', Contratar.as_view(), name="contratar"),
    url(r'^dashboard/contador', Dashboard.as_view(), name="contador"),
    url(r'^dashboard/me', DashboardUser.as_view(), name="me"),
    url(r'^registro', Registro.as_view(), name="registro"),
    url(r'^presupuesto', Presupuesto.as_view(), name="presupuesto"),
    url(r'^bienvenida', Bienvenida.as_view(), name="bienvenida"),
    url(r'^payment', Pago.as_view(), name="payment")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
