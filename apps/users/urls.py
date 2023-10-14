from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('signin/', views.SignInView.as_view(), name="signin"),
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('signout/', views.signout_view, name="signout"),
    path('password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
    path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='authentication/password-change-done.html'
    ), name="password_change_done"),
    path('password-reset/', views.UserPasswordResetView.as_view(), name="password_reset"),
    path('password-reset-confirm/<uidb64>/<token>/',
        views.UserPasswrodResetConfirmView.as_view(), name="password_reset_confirm"
    ),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='authentication/password-reset-done.html'
    ), name='password_reset_done'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='authentication/password-reset-complete.html'
    ), name='password_reset_complete'),

    path('profile/', views.profile, name='profile'),
]