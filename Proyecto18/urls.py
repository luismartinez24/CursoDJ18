from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'Proyecto18.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('app.urls')),
    url(r'^', include('app.urls')),
    url(r'^about', 'Proyecto18.views.about', name='about'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
]
