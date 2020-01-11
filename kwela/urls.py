from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from users import views as profile_views
from contact import views as contact_views
from django.contrib.sitemaps.views import sitemap
from listings.sitemaps import StaticViewSitemap
from realtors.sitemaps import StaticViewSitemap
from rentals.sitemaps import StaticViewSitemap
from houses.sitemaps import StaticViewSitemap





sitemaps = {
    'static': StaticViewSitemap
}



urlpatterns = [
    path('', include('pages.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    path('blog/',  include('blog.urls')),
    path('listings/', include('listings.urls')),
    path('accounts/', include('accounts.urls')),
    path('clients_payments/', include('client_payments.urls')),
    path('contact/', include('contact.urls')),
    path('contact/', contact_views.contact, name='contact'),
    path('houses/', include('houses.urls')),
    path('rentals/', include('rentals.urls')),
    path('team', include('team.urls')),    
    path('gallerys/', include('gallerys.urls')),
    path('jet/', include('jet.urls')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('profile/', profile_views.profile, name='profile' ),

    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


    