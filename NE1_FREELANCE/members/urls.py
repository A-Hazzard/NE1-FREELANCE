from django.urls import path, include
from . import views
from django.conf import settings

from django.conf.urls.static import static


urlpatterns = [
    
    path('login_user/', views.login_user, name='login'),
    path('signup_user/', views.register_user, name = "signup"),
    path('logout_user/', views.logout_user, name = "logout")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #used to link the static files ( css/js/images )
