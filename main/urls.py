
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView

from .routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include(router.urls)),
    path('api-auth/' , include('rest_framework.urls')),
    path('api/token/' , TokenObtainPairView.as_view()),
    path('api/token/refresh/' , TokenRefreshView.as_view()),
]
