from django.urls import path 
from . import views

urlpatterns = [
    path('search1',views.search1, name ='search1'),
    path('payment',views.payment, name ='payment'),
    path('booking2',views.booking, name ='booking'),
    path('booking1',views.booking1, name ='booking1'),
    path('confirmation',views.confirmation, name ='confirmation'),
    
    path('hospital',views.hosp2, name ='hospital'),
    path('oxygensup',views.oxygensup, name ='oxygensup'),
    path('oxlist',views.oxlist, name ='oxlist')

    


]
