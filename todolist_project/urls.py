from django.views.generic.base import TemplateView
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("accounts_app.urls")),
    path('', include('todolist_app.urls')),
    path('', TemplateView.as_view(template_name="home.html"), name="home"),
]