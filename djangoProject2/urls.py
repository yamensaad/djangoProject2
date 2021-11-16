"""djangoProject2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from cars import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns =  [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('index', views.bar_show),
    path('pie', views.pie_chart, name='pie'),
    path('bar', views.bar, name='bar'),
    path('line', views.line, name='line1'),
    path('line_plot', views.line_plot, name='line'),
    path('display', views.display ),
    path('pie_display', views.pie_display ),
    path('pie1' , views.pie_chart1),
    path('line_plot1' , views.line_chart1),
    path( 'bar1', views.bar1 ),


]

urlpatterns += staticfiles_urlpatterns()