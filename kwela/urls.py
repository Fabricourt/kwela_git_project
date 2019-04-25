from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from wasifu import views as wasifu_views
from contact.views import Contact
from malipo.views import Malipo
from django.contrib.sitemaps.views import sitemap
from listings.sitemaps import StaticViewSitemap
from testimonials.views import testimonial



sitemaps = {
    'static': StaticViewSitemap
}



urlpatterns = [
    path('', include('pages.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('blog/',  include('blog.urls')),
    path('catalog/',  include('catalog.urls')),
    path('listings/', include('listings.urls')),
    path('accounts/', include('accounts.urls')),
    path('contact/', Contact, name="contact"),
    path('contact/', include('contact.urls')),
    path('malipo/', include('malipo.urls')),
    path('admin/', admin.site.urls),
    path('wasifu/', wasifu_views.wasifu, name='wasifu' ),
    path('testimonial/', testimonial, name='testimonial'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


    