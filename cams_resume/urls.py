"""
URL configuration for cams_resume project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from home_page import views as home_view
from work_experience import views as work_view
from contact_me import views as contact_view

urlpatterns = [
    path('home/', home_view.home_page, name='home'),
    path('work_experience/', work_view.work_experience, name='work_experience'),
    path('contact_me/', contact_view.contact_me, name='contact_me'),
    path('admin/', admin.site.urls),
]
