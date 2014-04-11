from django.conf.urls import patterns, include, url
from django.contrib import admin
from nested_sample import views
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nested_formset_demo.views.home', name='home'),
    # url(r'^nested_formset_demo/', include('nested_formset_demo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^chainedselectchoices$',
        views.ChainedSelectChoices.as_view(),
        name = 'chained_select_choices'),
    url(r'^item/(?P<pk>\d+)/$', views.jsonno),
    # url('^$', views.ListBlocksView.as_view(), name='blocks-list'),
    # url('^blocks/new$', views.CreateBlockView.as_view(), name='blocks-new'),
    # url('^blocks/(?P<pk>\d+)/$', views.EditBuildingsView.as_view(),
    #     name='buildings-edit'),

)
