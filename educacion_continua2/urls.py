"""educacion_continua2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('ventas/personas_juridicas/', include("ventas.personas_juridicas.urls")),
	path('ventas/reporte_contacto/', include("ventas.reporte_contacto.urls")),
    path('ventas/personas_naturales/', include("ventas.personas_naturales.urls")),
    path('ventas/propuesta_corp/', include("ventas.propuesta_corp.urls")),
    path('ventas/proformas/',include("ventas.proformas.urls")),
    path('financiero/perfiles/', include('financiero.perfiles.urls')),
    path('financiero/ordenIngreso/',include('financiero.orden_ingreso.urls')),
    path('financiero/orden_facturacion/',include('financiero.orden_facturacion.urls')),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)