from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import PyShoURL

# Create your views here.

def pysho_redirect_view(request, shortcode=None, *args, **kwargs):  # function based view FBV
    # getting real url or if it not exists we get 404 page
    obj = get_object_or_404(PyShoURL, shortcode=shortcode)
    return HttpResponseRedirect(obj.url)

class PyShoCBView(View):  # class based view CBV
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(PyShoURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)

