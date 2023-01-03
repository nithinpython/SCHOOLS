from . import views
from django.urls import path

urlpatterns = [
    path('', views.demo, name='demo'),
    path('about', views.about, name='about'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('reg_one', views.reg_one, name='reg_one'),
    path('pending', views.pending, name="pending"),
    path('demo',views.demo2, name='demo2'),

]
