"""
URL configuration for playground project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [

    # rutas de la vista de inicio
    path('', include('core.urls')),

    # urls de pages del crud
    path('pages/', include('pages.urls')),


    # rutas para las autenticaciones de login logout y mas
    path('accounts/', include('django.contrib.auth.urls')),

    # aqui crearemos con las rutas de accounts las de registro y mas
    path('accounts/', include('registration.urls')),

    # aqui crearemos con las rutas de accounts las de registro y mas
    path('profiles/', include('profiles.urls')),


    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
