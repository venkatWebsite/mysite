from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about-ven kat/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
]