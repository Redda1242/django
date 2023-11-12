"""
URL configuration for raghd_ca project.

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
from django.urls import path
from searchCountry import views
from searchCountry.views import find_nearby_countries  # assuming you have these view functions

urlpatterns = [
    path('admin/', admin.site.urls),
    path('find_nearby_countries/<str:lat>/<str:lon>/<str:distance>/', views.find_nearby_countries, name='find_nearby_countries'),
    path('', views.home, name='home'),
    path('map/', views.map_view, name='map'),  # URL pattern for the map page
    path('find_nearby_countries/', views.find_nearby_countries, name='find_nearby_countries'),
]

