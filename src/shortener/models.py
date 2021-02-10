from django.conf import settings
from django.db import models

from django_hosts.resolvers import reverse
from .utils import code_generator, create_shortcode
from .validators import validate_url, validate_dot_com

# getting max length from settings
SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)


# Create your models here.

class PyShoURL(models.Model):
    url = models.CharField(max_length=220, validators=[validate_url, validate_dot_com])  # taking url with  charField
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)  # shortened address def value 'defshortcode'
    updated = models.DateTimeField(auto_now=True)  # everytime the model is saved (for testing)
    timestamp = models.DateTimeField(auto_now_add=True)  # when model was created (for testing)
    active = models.BooleanField(default=True)  # URL is active?

    # override default save method
    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        # adding http if link is without it
        if not "http" in self.url:
            self.url = "http://" + self.url
        super(PyShoURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)

# getting complete short url address
    def get_short_url(self):
        print(self.shortcode)
        url_path = reverse("scode", kwargs={'shortcode': self.shortcode}, host='www', scheme='http')
        return url_path
