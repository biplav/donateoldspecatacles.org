from django.conf.urls import patterns, url

from workflow import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^how$', views.how, name='how'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^ngo$', views.ngo, name='ngo'),
    url(r'^optical$', views.optical, name='optical'),
    url(r'^corporate$', views.corporate, name='corporate'),
    url(r'^search$', views.search, name='search')
)
