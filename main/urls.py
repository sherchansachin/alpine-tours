from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path('packages/', views.packages, name='packages'),
    path('package-details/<slug:slug>/', views.package_detail, name='package_info'),
]