from django.urls import path
from.import views



urlpatterns = [
    
    path('',views.index),
    path('xyz/',views.click),
    path('logout/',views.logout),
    path('about/',views.about),
    
    path('login/',views.login,name="loginpage"),
    path('register/',views.register,name='registerpage'),
    
    
]