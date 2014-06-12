from django.conf.urls import patterns, include, url

from django.contrib import admin
import files.urls

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MyYun_py.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^files/', include(files.urls)),
)
