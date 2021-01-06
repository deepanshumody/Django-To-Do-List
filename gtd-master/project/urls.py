from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = (
    [
        path("", auth_views.LoginView.as_view(), name="login"),
        path("logout", auth_views.LogoutView.as_view(), name="logout"),
        path("gtdadmin/", admin.site.urls),
        path("todo/", include("todo.urls", namespace="todo")),
        path("accounts/", include('allauth.urls')),
        path("send_email/", TemplateView.as_view(template_name="email.html"), name="email"),


    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
