from django.urls import path
from . import views


urlpatterns=[
    path('',views.about2,name='aboutpage'),
    path('cmt/',views.cmt),
    path('like/',views.like),
]