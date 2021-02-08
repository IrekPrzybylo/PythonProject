"""PySho URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from shortener.views import pysho_redirect_view, PyShoCBView


urlpatterns = [
    path('admin/', admin.site.urls),
    # path(r'^(?P<slug:shortcode>{6,15})$', pysho_redirect_view),
    path('a/<slug:shortcode>', pysho_redirect_view),
    path('b/<slug:shortcode>', PyShoCBView.as_view()),
]
