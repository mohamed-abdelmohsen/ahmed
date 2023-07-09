from django.urls import path
from . import views


urlpatterns=[
    path('',views.home,name='home'),
    path('reservation/',views.reservation,name='reservation'),
    path('login/',views.signin,name='signin'),
    path('logout/',views.signout,name='signout'),

]