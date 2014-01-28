from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from park_app import views

print(views)

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index, name='index'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
