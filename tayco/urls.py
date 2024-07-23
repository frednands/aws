
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from . import views
admin.site.site_title = 'Admin'
admin.site.site_header = 'Tayco'
admin.site.index_title = 'Tayco Administration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home' ),
    path('project/',include('project.urls') ),
    path('project/',include('project.urls') ),
    path('user/',include('authentification.urls')),
    path('verify/',include('authentification.urls')),
    path('about/',views.about,name='about'),
    path('contact/',views.contact ,name='contact'),
    path('user/',include('authentification.urls')),
    path('accounts/', include('allauth.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('profiles/', include('profiles.urls')),  # Include profile app URLs
    
   
]

urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

handler404 = "error.views.handle_not_found"
handler500 = "error.views.handle_server_error"
