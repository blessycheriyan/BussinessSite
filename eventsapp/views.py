

from django.contrib import messages
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from eventsapp.forms import  SubscribeForm
# Create your views here.
from eventsapp.models import user

def event2(request):
    return render(request,'event2.html')

def event3(request):
    return render(request,'event3.html')
def event4(request):
    return render(request,'event4.html')
def index(request):
    return render(request,'index.html')

def event4q(request):
    return render(request,'index.html')
def home(request):
    return render(request,'index.html')
def blog(request):
    return render(request, 'blog.html')
def userpage(request):
    return render(request, 'userpage.html')

def sample(request):
    return render(request,'profile.html')
def register(request):
 try:

    if request.method == 'POST':
        uname1=request.POST['uname']
        name1 = request.POST['name']
        lastname1 = request.POST['lastname']
        email1 = request.POST['email']
        password1 = request.POST['password']
        confirmpassword1 = request.POST['confirmpassword']
        c = request.POST['city']
        d = request.POST['address']
        e = request.POST['contactno']
        g = request.POST['gender']
        if password1 == confirmpassword1:
            if user.objects.filter(email=email1).exists() and user.objects.filter(name=name1).exists():


                return render(request, 'register.html', {'error1': "Email and username taken"})

            if user.objects.filter(name=name1).exists():
                messages.info(request, 'Username taken')
                return render(request, 'register.html', {'error2': "username taken"})


            else:


                register1 = user(name=name1,uname=uname1, lastname=lastname1, email=email1, password=password1, city=c,address=d,contactno=e, gender=g)
                register1.save();


                return render(request, 'register.html',{'error': "Succesfully Registered"})
        else:

            return render(request, 'register.html', {'error2': "Password not matching"})


    else:

        return render(request,'register.html')
 except:

             return render(request, 'register.html', {'error': "Please Fill The Form"})


def profile(request):
 try:

     a =  request.session['updateuser']
     userlist = user.objects.filter(name=a)


     if request.method == 'POST':
         name1 = request.POST['name']
         uname1= request.POST['uname']
         lastname1 = request.POST['lastname']
         email1 = request.POST['email']
         password1 = request.POST['password']
         confirmpassword1 = request.POST['confirmpassword']
         c = request.POST['city']
         d = request.POST['address']
         e = request.POST['contactno']
         g = request.POST['gender']
         if password1 == confirmpassword1:



            user.objects.filter(name=a).update(name=name1,uname=uname1, lastname=lastname1, email=email1, password=password1, city=c, address=d,

                          contactno=e, gender=g)


         return render(request, 'profile.html',{'user': userlist,'error': "Change Saved Successfully"})

     else:
         return render(request, 'profile.html', {'user': userlist})
 except:

             return render(request, 'profile.html', {'error': "Please Fill The Form"})


def login(request):
    try:


         if request.method=="POST":
            m=user.objects.get(email=request.POST['email'])


            if m.password==request.POST['passw']:
                request.session['updateuser']=m.name



                return render(request,'userpage.html',{'name':m.name})

            else:
                print("hello")
                return render(request, 'login.html',{'error':"Please check Email and Password"})

         else:
             print("hell")
             return render(request, 'login.html')
    except:

        return render(request, 'login.html', {'error1': "Please Fill The Form"})

def event1(request):
    return render(request,'event1.html')


def logout(request):
        try:
            del request.session['users_name']
        except KeyError:
            pass
        return render(request, 'index.html')

def resetpassword(request):
    a = request.session['updateuser']
    userlist = user.objects.filter(name=a)

    if request.method == 'POST':

        password1 = request.POST['password']
        confirmpassword1 = request.POST['confirmpassword']
        if password1 == confirmpassword1:

            user.objects.filter(name=a).update(password=password1)
        return render(request, 'resetpassword.html', {'user': userlist, 'error': "Change Saved Successfully"})
    else:
        return render(request, 'resetpassword.html', {'user': userlist})


def subscribe(request):
    form=SubscribeForm()
    if request.method=='POST':
        form=SubscribeForm(request.POST)
        if form.is_valid():
            subject='Reset Password Request'
            message= 'Please Click this link and Change Password - http://127.0.0.1:8000/resetpassword'




            receipient=form.cleaned_data.get('email')
            send_mail(subject,message,settings.EMAIL_HOST_USER,[receipient],fail_silently=False)
            messages.success(request,'Success!')
            return redirect('subscribe')
    return render(request,'email.html',{'form':form})