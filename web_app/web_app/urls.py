from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
    path('api-token-auth/', views.obtain_auth_token),
    path('', include('website.urls', namespace='posts')),
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
]

handler404 = 'core.views.page_not_found'

handler403 = 'core.views.csrf_failure'

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
