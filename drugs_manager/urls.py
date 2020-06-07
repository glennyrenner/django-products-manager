"""drugs_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from main import views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.home, name='home'),
    path('request_entries/', main_views.request_entries, name='request-entries'),
    path('add_drug/', main_views.add_drug, name='add-drug'),
    path('add_sale/', main_views.add_sale, name='add-sale'),
    path('add_entry/', main_views.add_entry, name='add-entry'),
    path('save_entry/', main_views.save_entry, name='save-entry'),
    path('get_product_info/', main_views.get_prod_info, name='get-product-info'),
    path('save_sale/', main_views.save_sale, name='save-sale'),
    path('get_drugs_list/', main_views.get_drugs_list, name='get-drugs-list'),
    path('get-drug-details/', main_views.get_drug_details, name='get-drug-details'),
]