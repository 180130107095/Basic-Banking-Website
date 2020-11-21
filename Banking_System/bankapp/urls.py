from django.contrib import admin
from django.urls import path
from bankapp import views

urlpatterns = [
    path('', views.index, name='home'),
    path('transfer_credit', views.transfer_credit, name='transfer_credit'),
    path('user_final',views.user_final,name='user_final'),
    path('user/<str:name>', views.user, name='user'),
    path('user/<str:name>/confirmation', views.confirmation, name='confirmation'),
    

]
