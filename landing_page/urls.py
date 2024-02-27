from django.urls import path,include
from . import views

urlpatterns = [
    
    path('',views.index,name="index"),
    path('admin_login',views.admin_login,name="admin_login"),
    path('admin_logout',views.admin_logout,name="admin_logout"),
    path('contact_list',views.contact_list,name="contact_list"),
    path('delete_contact/<int:pk>',views.delete_contact,name="delete_contact"),
]