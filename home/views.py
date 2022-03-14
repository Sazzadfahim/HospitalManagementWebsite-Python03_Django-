from django.shortcuts import render, redirect
from .models import oxygensupply
from .models import doctor
from .models import bookingjs
from .models import consult
from .models import record
from .models import user_profile
from .forms import user_profile_form
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

from django.contrib import messages



# Create your views here.

def home(request):
    return render(request, "home.html")



def oxygen(request):
    infos = oxygensupply.objects.all()



   
    return render(request, "Oxy_list.html", {'infos' : infos})



def consult1(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        message = request.POST['message']
        dept = request.POST['dept']
        
        
        ref = consult(first_name=first_name, last_name=last_name,  email=email, message=message, dept=dept )
        ref.save()
        
        
        return render(request, "consultation_form.html")
        

    else:
        return render(request, "consultation_form.html")


def consult2(request):

    infos = doctor.objects.all()


    return render(request, "consult_data.html",{'infos' : infos})



def home2(request):

    return render(request, "home3.html")




def bookingjs1(request):
    if request.method == 'POST':
        hospitsl_name = request.POST['hospitsl_name']
        booking_type = request.POST['booking_type']
        name = request.POST['name']
        email = request.POST['email']
        phone_no = request.POST['phone_no']
       
        ref = bookingjs(hospitsl_name=hospitsl_name, booking_type=booking_type,  name=name, email=email, phone_no=phone_no)
        ref.save()
        return render(request, 'bookjs.html')

    else:

        return render(request, 'bookjs.html')




def profile(request):
   #user = auth.authenticate(username=username,password=password)
     # if user is not None:
        # auth.login(request, user)
         infos = user_profile.objects.all()
         return render(request, "profile.html",{'infos' : infos})
   
    
def edit_pro(request):
 user_profile = request.user.user_profile
 form = user_profile_form(instance=user_profile)
 if request.method == 'POST':
  form = user_profile_form(request.POST, request.FILES,instance=user_profile)
 if form.is_valid():
   form.save()
 context = {'form':form}
 return render(request, 'edit_pro.html', context)
 


def edit_style(request):

    return render(request, "edit_style.html")




def record1(request):

    if request.method == 'POST':
        
        name = request.POST['name']
        email = request.POST['email']
        RoomNo = request.POST['RoomNo']
       
        ref = record(name=name, email=email, RoomNo=RoomNo)
        ref.save()
        template = render_to_string('email_tem.html', {'RoomNo': RoomNo})
        
        email = EmailMessage(
            'Booking confirmation',
            template,
            settings.EMAIL_HOST_USER,
            [email]
        )
        email.fail_silently=False
        email.send()


        return render(request, 'record.html')

    else:

        return render(request, 'record.html')



