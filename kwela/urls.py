from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as profile_views
from contact.views import Contact
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
    path('listings/', include('listings.urls')),
    path('accounts/', include('accounts.urls')),
    path('contact/', Contact, name="contact"),
    path('contact/', include('contact.urls')),
    path('fundis/', include('fundis.urls')),
    path('women/', include('women.urls')),
    path('msuppliers/', include('msuppliers.urls')),
    path('admin/', admin.site.urls),
    path('profile/', profile_views.profile, name='profile' ),
    path('testimonial/', testimonial, name='testimonial'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


    