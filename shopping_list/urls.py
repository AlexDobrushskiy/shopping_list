from django.conf.urls import patterns, include, url
from django.contrib import admin
from main.views import ShoppingView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shopping_list.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', ShoppingView.as_view()),
)
