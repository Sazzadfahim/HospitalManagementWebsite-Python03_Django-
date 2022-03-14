from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home2, name ='home'),
    path('oxygen',views.oxygen, name ='oxygen'),
    path('consult',views.consult1, name ='consult'),
    path('consult2',views.consult2, name ='consult2'),
    path('booking11',views.bookingjs1, name ='bookingjs1'),
    path('profile',views.profile, name='profile'),
    path('edit_pro',views.edit_pro, name='edit_pro'),
    path('edit_style',views.edit_style, name='edit_style'),
    path('record',views.record1, name='record')
    

]
