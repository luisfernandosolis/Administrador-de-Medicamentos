
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
   	path('', include('apps.medicamentos.urls')),
   	path('user/', include('apps.user.urls')),
]
