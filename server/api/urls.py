from django.urls import path
from . import views
from .views import RegisterView, LoginView,  DoctorLoginView, BookingView, CheckAvailabilityView


urlpatterns = [
    path('', views.home, name='home'),
    path('register/',  RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('booking/', BookingView.as_view(), name='booking'),
    path('doctor/login/', DoctorLoginView.as_view(), name='doctor-login'),
    path('check-availability/', CheckAvailabilityView.as_view(), name='check-availability'),
    path('user-profile/', views.user_profile, name='user-profile'),
]
