from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from api.views import CustomAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("api.urls")),
    path('api-auth/', include('rest_framework.urls')),
    # path('auth/user/', include('djoser.urls.authtoken')),
    path('api-token-auth/', CustomAuthToken.as_view()),
]


'''
/auth/user/token/login (POST) => returns user auth_token
/auth/user/token/logout (GET)
'''