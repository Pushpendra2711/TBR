
from django.urls import path
from .views import UserLogin,UserSignup,ProtectedApiView
from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView


urlpatterns = [
    path('login/',UserLogin.as_view(),name="UserLogin"),
    path('signup/',UserSignup.as_view(),name="UserSignup"),
    path('protected/',ProtectedApiView.as_view(),name="protected_api"),

    #jwt tokens view
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("token/refresh/",TokenRefreshView.as_view(),name="refresh_token")
    ]