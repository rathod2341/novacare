"""
URL configuration for novacare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from client import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('', views.index, name='index'),
    path('index2/',views.index2),
    path('login/',views.login),
    path('register/',views.register),
    path('time-table/',views.time_table),
    path('doctors/',views.doctors),
    path('doctors/<int:sid>/<int:aid>',views.doctors),
    #path('doctors/<int:aid>',views.doctors),
    path('doctors-details/<int:id>', views.doctors_details),
    path('service/<int:id>', views.service),
    path('service-details/', views.service_details),
    path('about/', views.about),
    path('testimonials/', views.testimonials),
    path('mail-success/', views.mail_success),
    path('blog-grid/<int:id>', views.blog_grid),
    path('blog-single/', views.blog_single),
    path('faq/', views.faq), 
    path('pricing/', views.pricing),
    path('contact/', views.contact),
    path('error404/', views.error404, name='error404'),
    path('error404-2/', views.error404_2, name='error404_2'),
    path('clear_filter/',views.clear_filter),
    path('appointment/<int:id>', views.appointment),  
    path('insert_review/<int:id>',views.insert_review),
    path('logout/',views.logout),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)