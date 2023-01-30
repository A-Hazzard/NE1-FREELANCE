"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

from django.conf import settings
from django.conf.urls.static import static

from home import views as home_view
from aboutus import views as about_view
from searchResults import views as search_results

urlpatterns = [
    path('',home_view.index, name = 'home_page'), #ne1freelance.com - Home page
    path('search/', search_results.search_jobs, name = 'search_jobs'), #ne1freelance.com/search - Search page displaying jobs
    path('createjob/', include("createjob.urls"), name = 'create_job'), #ne1freelance.com/createjob - Displays the job form
    path('aboutus/',about_view.aboutus, name = 'about_us'), #ne1freelance.com/aboutus - Displays the about us page
    path('admin/', admin.site.urls), #ne1freelance.com/admin - Displays the admin page
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #used to link the static files ( css/js/images )
