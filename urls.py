from ecomstore import settings
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^ecomstore/', include('ecomstore.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
		(r'^', include('catalog.urls')),
		(r'^cart/', include('cart.urls')),
		(r'^catalog/$', 'preview.views.home'),
)

handler404 = 'ecomstore.views.file_not_found_404'
		
if settings.DEBUG:
	urlpatterns += patterns('',
				(
				r'^static/(?P<path>.*)$', 'django.views.static.serve',
					{ 'document_root' : '/Users/duy/Sites/www/html/ecomstore/static' }),
				)
