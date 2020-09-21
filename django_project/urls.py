from django.contrib import admin
from django.urls import path,include
from users import views as users_views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls') ),
    path('register/',users_views.register,name='register'),
    path('accounts/', include('users.urls') ),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'  ),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'  ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

