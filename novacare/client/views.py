from client.models import User , Doctor , Services , Review , Appointment , galllery , specialization , Area
from django.shortcuts import redirect , render
from django.contrib import messages
from client.models import Doctor



def index(request):
    d = Doctor.objects.all().count()
    s = specialization.objects.all().count()
    p = User.objects.all().count()
    a = Appointment.objects.all().count()

    special = specialization.objects.all()
    doc = Doctor.objects.all()

    return render(request, "index.html",{'Doctor':d,'Specialization':s,'User':p,'Appoitment':a,'sp':special,'doctor':doc})

from django.contrib import messages

def login(request):
    if request.method == "POST":
        uname = request.POST.get('email')
        pwd = request.POST.get('password')
        print(uname,"-------",pwd)

        c = User.objects.filter(email=uname , password = pwd).count()
        if c == 1:
            u = User.objects.get(email=uname , password = pwd)
            request.session['user_id'] = u.user_id
            print("----------session check -----------",request.session['user_id'])
            return redirect("/doctors/")

        else:
            messages.error(request,"invalid username or password")
            return render(request,"login.html") 
    else:
        return render(request, "login.html")

def register(request):
    if request.method == "POST":

        User.objects.create(
            user_name=request.POST.get('user_name'),
            email=request.POST.get('email'),
            password=request.POST.get('password'),
            contact_no=request.POST.get('contact'),
            area_id_id=request.POST.get('area'),
            otp=0,
            otp_used=0
        )
            
        return redirect("/login")
        
    else:
        a = Area.objects.all() 
        return render(request, "register.html",{'area':a})

def index2(request):
    return render(request, "index.html")

def time_table(request):
    u=  request.session['user_id']
    obj = Appointment.objects.filter(patient_id=u)
    return render(request, "time-table.html",{'app':obj})

def doctors(request, sid=0, aid=0):

    print('--',sid,'--',aid)
    # Store selected values in session
    if sid != 0:
        request.session['spe'] = sid

    if aid != 0:
        request.session['area'] = aid

    # Get values from session if not passed
    if sid == 0:
        sid = request.session.get('spe', 0)
    
    if aid == 0:
        aid = request.session.get('area', 0)


    print("--------------Specialization-------------",sid)
    print("==================AREA=================",aid)

    obj = Doctor.objects.all()

    if sid != 0:
        obj = obj.filter(sp_id=sid)

    if aid != 0:
        obj = obj.filter(area_id=aid)

    return render(request, "doctors.html", {'doc': obj})

def clear_filter(request):
    request.session.pop('spe', None)
    request.session.pop('area', None)
    return redirect('/doctors/')   # Replace with your URL name

def doctors_details(request,id):
    d = Doctor.objects.get(doctor_id=id)
    s = Services.objects.filter(doctor_id=id)
    r = Review.objects.filter(doctor_id=id)
    return render(request,"doctor-details.html",{'doc':d,'serv':s,'reviews':r})       

def service(request,id=0):
    s = Services.objects.filter(doctor_id=id)
    return render(request,"service.html",{'s':s})
    
def service_details(request):
    return render(request,"service-details.html")  

def about(request):
    return render(request,"about.html")  

def testimonials(request):
    return render(request,"testimonials.html")        

def mail_success(request):
    return render(request,"mail-success.html")   

def blog_grid(request,id=0):
    obj = galllery.objects.filter(doctor_id=id)
    return render(request,"blog-grid.html",{'gallery':obj})

def blog_single(request):
    return render(request,"blog-single.html")

def faq(request):
    return render(request,"faq.html")

def pricing(request):
    return render(request,"pricing.html")

def contact(request):
    return render(request,"contact.html")

def error404(request):
    return render(request, "404.html")

def error404_2(request):
    return render(request, "404-2.html")

def appointment(request,id=0):
    
    if 'user_id' not in request.session:
        return redirect("/login/")

    if request.method == "POST":
        u=  request.session['user_id']
        Appointment.objects.create(
        patient_id_id=u,
        doctor_id_id=id,
        description=request.POST.get('message'),
        Appointment_date=request.POST.get('appdate'),
        Appointment_time=request.POST.get('apptime'),
        payment_mode='None'
        )
       
        messages.success(request, "appointment successful")
        return redirect("/time-table/") 

    else:
        return render(request, "appointment.html")

def insert_review(request,id=0):

    if 'user_id' not in request.session:
        return redirect("/login/")

    if request.method == "POST":
        u=  request.session['user_id']
        Review.objects.create(
            patient_id_id=u,
            doctor_id_id=id,
            description=request.POST.get('message')  
        )
        return redirect('/index2/')
    else:
        return render(request,'insert_review.html')


def logout(request):
    try:
        del request.session['user_id']
        return redirect("/login/")
    except:
        pass