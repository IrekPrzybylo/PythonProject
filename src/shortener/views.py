from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.

def pysho_redirect_view(request, shortcode=None, *args, **kwargs):  # function based view FBV
    return HttpResponse("hello {sc}".format(sc=shortcode))

class PyShoCBView(View):  # class based view CBV
    def get(self, request, shortcode=None, *args, **kwargs):
        return HttpResponse("hello again {sc}".format(sc=shortcode))

