from django.shortcuts import render, redirect
from .models import information
from .models import hospital
from .models import booking1





# Create your views here.











def booking(request):
    if request.method == 'POST':
        hospitsl_name = request.POST['hospitsl_name']
        booking_type = request.POST['booking_type']
        name = request.POST['name']
        email = request.POST['email']
        phone_no = request.POST['phone_no']
        payment_type = request.POST['payment_type']
        card_no = request.POST['card_no']
        bkash_no = request.POST['bkash_no']
        address = request.POST['address']
        ref = booking1(hospitsl_name=hospitsl_name, booking_type=booking_type,  name=name, email=email, address=address, bkash_no= bkash_no, card_no=card_no, payment_type=payment_type, phone_no=phone_no )
        ref.save()
        return redirect('/')

    else:

        return render(request, "booking_js.html")

def payment(request):
    return render(request, "hosinfo_index3.html")
    

def search1(request):

    infos = information.objects.all()



    return render(request, "hosinfo_index.html",{'infos' : infos})


def confirmation(request):
    return render(request, "confirmation.html")



def hosp2(request):

    
    dests = hospital.objects.all()

    return render(request, "searching.html",{'dests' : dests})



def oxygensup(request):
    return render(request, "oxygen supply.html")

def oxlist(request):
    return render(request, "oxy_list.html")















   
    




