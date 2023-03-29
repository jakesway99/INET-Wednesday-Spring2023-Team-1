from django.urls import include, path, re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register", views.register_request, name="register"),
    path("login", views.login_view, name="login"),
    path("activate/<uidb64>/<token>", views.activate, name="activate"),
    path("logout/", views.logout_view, name="logout"),

    # reset password urls
    path("reset_password/", auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"), 
    name="password_reset"),

    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"), 
    name="password_reset_done"),

    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), 
    name="password_reset_confirm"),

    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"), 
    name="password_reset_complete"),
]
