"""
URL configuration for Project_1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from Project_1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
     # static urls
    path('about-us/',views.aboutus),
    path('about/',views.about, name="about"),
    path('course/',views.course),
    path('course/<courseid>',views.courseDetails),
    path('',views.homePage, name="home"),
    path('contact/',views.contact, name="contact"),
    path('form/',views.form),
    path('submitform/',views.submitform, name="submitform" ),
    path('calculator/', views.calculator),
    path('evenodd/', views.evenodd),
    path('marksheet', views.marksheet),
    path('sendmail', views.sendmail),
    path('services/', views.services, ),
]

if(settings.DEBUG):
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)