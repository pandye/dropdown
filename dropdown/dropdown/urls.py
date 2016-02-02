from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dropdown.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^dropdown/$', 'dropdown.views.dropdown', name='dropdown'),
    url(r'^state_ajax/$', 'dropdown.views.state_ajax', name='state_ajax'),
)
