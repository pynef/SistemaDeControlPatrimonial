from django.conf.urls import patterns, include, url


urlpatterns = patterns('SistemaDeControlPatrimonial.app.institucion.views',
	url(r'^instituciones/$','instituciones'),
	url(r'^instituciones/(?P<ids>\d+)/$','instituciones'),
)