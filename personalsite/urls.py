from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from django.contrib import admin
from django.views.generic import TemplateView
from personalsite.settings import MEDIA_ROOT

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', TemplateView.as_view(template_name='base.html'), name="home"),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': MEDIA_ROOT}),
)