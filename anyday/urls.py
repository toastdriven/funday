from django.conf.urls import patterns, include, url
from django.contrib import admin

from core.views import RandomFundayView, RaceRandomFundayView


admin.autodiscover()

urlpatterns = patterns(
    '',  # View prefix
    url(r'^$',
        RandomFundayView.as_view(template_name='home.html'),
        name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<race>\w+)/$',
        RaceRandomFundayView.as_view(),
        name='random_race'),
)
