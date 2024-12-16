from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('register/', views.register_request, name='register'),
    path('user-profile/', views.user_profile_view, name='user_profile_view'),
    path('profile-details/', views.profile_details_view, name='profile_details_view'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('change-password/', views.change_password, name='change_password'),
]
