from django.conf.urls import url

from . import views

app_name = 'artist'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^gallery/', views.gallery, name='gallery'),
	url(r'^about/', views.about, name='about'),
	url(r'^contact/', views.contact, name='contact'),
]
