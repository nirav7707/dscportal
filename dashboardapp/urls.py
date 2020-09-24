from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns=[
    #authentication routes
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logoutUser,name='logout'),

    #view route
    path('',views.dashboard,name='dashboard'),
    path('data/<str:id>',views.datalist,name='datalist'),
    path('createdata/<str:id>/',views.createdata,name='createdata'),
    path('deletedata/<str:id>/<str:cat>',views.deletedata,name='deletedata'),
    path('updatedata/<str:id>/<str:cat>',views.updatedata,name='updatedata'),
    path('event/<str:cat>/',views.event,name='event'),

    #password reset
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), 
        name="password_reset_complete"),

]