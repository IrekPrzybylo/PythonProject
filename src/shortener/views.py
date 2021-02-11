from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views import View

from analytics.models import ClickEvent
from .forms import SubmitUrlForm
from .models import PyShoURL


# Create your views here.

class HomeView(View):
    """
    Basic Home class view
    """
    def get(self, request, *args, **kwargs):
        """
        Home page
        :return:
        Returns a HttpResponse object combining home page template and context
        """
        the_form = SubmitUrlForm()
        context = {
            "title": "PySho.rt",
            "form": the_form
        }
        return render(request, "shortener/home.html", context)

    # post method
    def post(self, request, *args, **kwargs):
        """
        Post method
        Submits completed form if its properly completed
        :return:
        If Created: render Success page with content
        Else: render Already-exists page
        Returns a HttpResponse object combining template and context
        """
        form = SubmitUrlForm(request.POST)
        context = {
            "title": "PySho.rt",
            "form": form
        }
        template = "shortener/home.html"
        if form.is_valid():
            new_url = form.cleaned_data.get("url")
            obj, created = PyShoURL.objects.get_or_create(url=new_url)
            context = {
                "object": obj,
                "created": created,
            }
            if created:
                template = "shortener/success.html"
            else:
                template = "shortener/already-exists.html"

        return render(request, template, context)


class URLRedirectView(View):  # class based view CBV
    """
    Redirect View
    """
    def get(self, request, shortcode=None, *args, **kwargs):
        """
        Redirects to page
        :param shortcode: shortcode set to None
        If shortened url does not exist in queryset raise 404 error and redirecting to error404 page
        Otherwise redirecting to original "long url" page
        """
        qs = PyShoURL.objects.filter(shortcode__iexact=shortcode)
        if qs.count() != 1 and not qs.exists():
            raise Http404
        obj = qs.first()
        print(ClickEvent.objects.create_event(obj))
        return HttpResponseRedirect(obj.url)
