from django.urls import path, re_path
from .views import wildcard_redirect
urlpatterns = [
    re_path(r'^(?P<path>.*', wildcard_redirect),
    # path(r'^(?P<slug:shortcode>{6,15})$', pysho_redirect_view),
]
