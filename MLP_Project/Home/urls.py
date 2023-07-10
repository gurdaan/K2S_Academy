from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('', views.index,name='Home'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('contact',views.contactUs,name='contact'),

    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('loginlogoutbutton',views.loginlogoutbutton,name='loginlogoutbutton'),
    path('registeration',views.registeration,name='registeration'),

    path('password_reset/', views.password_reset, name='password_reset'),
    path('password_reset/done/', views.password_reset_done, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('reset/done/', views.password_reset_complete, name='password_reset_complete'),

    path('add_notice/', views.add_notice, name='add_notice'),
    path('edit_notice/<int:notice_id>/', views.edit_notice, name='edit_notice'),
    path('delete_notice/<int:notice_id>/', views.delete_notice, name='delete_notice'),
    path('admin/', admin.site.urls)
]
