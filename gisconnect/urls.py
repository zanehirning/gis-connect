from django.contrib import admin
from django.urls import path
from django.contrib.auth import views
from core.views import frontpage, signup


urlpatterns = [
    path('', frontpage, name="frontpage"),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('signup/', signup, name="signup"),
    path("admin/", admin.site.urls),
]
