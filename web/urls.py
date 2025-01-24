from django.urls import path
from .views import *
from django.contrib.sitemaps.views import sitemap
from .sitemaps import *
from django.views.generic.base import TemplateView

app_name = "web"

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('', home, name='home'),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt/', TemplateView.as_view(template_name='web/robots.txt', content_type='text/plain')),

    path('contacto/', contacto, name='contacto'),
    path('membresia/', membresia, name='membresia'),
]