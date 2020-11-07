from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.http import HttpResponse
# Create your views here.

def index(request):
    if request.method == "POST":
        global name
        global phone
        global pick
        global drop
        global drop
        global car
        global date
        global time
    
        name = request.POST['nm']
        phone = request.POST['em']
        pick = request.POST['ph']
        drop = request.POST['pi']
        car = request.POST['dr']
        date = request.POST['tm']
        time = request.POST['dt']
        
        


  
        #send an email

        return render(request, 'index.html', {'name': name})
        
    else:
        return render(request, 'index.html')
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def destinations(request):
    return render(request, 'destinations.html')

def destinations2(request):
    return render(request, 'destinations2.html')

def destinations3(request):
    return render(request, 'destinations3.html')

def destinations4(request):
    return render(request, 'destinations4.html')

def destinations5(request):
    return render(request, 'destinations.html')

def dest6(request):
    return render(request, 'dest6.html')

def bk(request):
    if request.method == "POST":
        global name
        global phone
        global pick
        global drop
        global drop
        global car
        global date
        global time
    
        name = request.POST['nm']
        phone = request.POST['em']
        pick = request.POST['ph']
        drop = request.POST['pi']
        car = request.POST['dr']
        date = request.POST['tm']
        time = request.POST['dt']
        
        


  
        #send an email

        return render(request, 'bk.html', {'name': name})
        
    else:
        return render(request, 'bk.html')

def bk(request):
    if request.method == "POST":
        global name
        global phone
        global pick
        global drop
        global drop
        global car
        global date
        global time
    
        name = request.POST['nm']
        phone = request.POST['em']
        pick = request.POST['ph']
        drop = request.POST['pi']
        car = request.POST['dr']
        date = request.POST['tm']
        time = request.POST['dt']
        
        


  
        #send an email

        return render(request, 'bk.html', {'name': name})
        
    else:
        return render(request, 'bk.html')

def contact(request):
    if request.method == "POST":
        global name
        global email
        global subject
        global sug
        
    
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        sug = request.POST['sug']
        
        
        


  
        #send an email
        send_mail(

            name ,#subject
            "name: "+name+'\n'+"email: "+email+'\n'+"subject: "+subject+'\n'+"suggestion: "+sug,# message
            # from mail
            'sarigecabs@gmail.com',
            
            ['sarigecabs@gmail.com'],# to mail
        )

        return render(request, 'contact.html', {'name': name})
        
    else:
        return render(request, 'contact.html')

def sm1(request):
    if request.method == "POST":
        
        
        #send an email
        send_mail(

            name ,#subject
            "name: "+name+'\n'+"phone no: "+phone+'\n'+"pick: "+pick+'\n'+"drope: "+drop+'\n'+"car: "+car+'\n'+"date: "+date+'\n'+"time: "+time+'\n'+"vehical:HATCHBACK"+'\n'+"AC:RS "+'\n'+"NON AC:RS ",# message
            # from mail
            'sarigecabs@gmail.com',
            
            ['sarigecabs@gmail.com'],# to mail
        )
        
    return render(request, 'email.html', {'name': name})

def sm2(request):
    if request.method == "POST":
        #send an email
        
        send_mail(

            name ,#subject
            "name: "+name+'\n'+"phone no: "+phone+'\n'+"pick: "+pick+'\n'+"drope: "+drop+'\n'+"car: "+car+'\n'+"date: "+date+'\n'+"time: "+time+'\n'+"vehical:SEDAN(4+1)"+'\n'+"AC:RS "+'\n'+"NON AC:RS ",# message
            # from mail
            'sarigecabs@gmail.com',
            
            ['sarigecabs@gmail.com'],# to mail
        )
    return render(request, 'email.html', {'name': name})
def sm3(request):
    if request.method == "POST":
        #send an email
        send_mail(

            name ,#subject
            "name: "+name+'\n'+"phone no: "+phone+'\n'+"pick: "+pick+'\n'+"drope: "+drop+'\n'+"car: "+car+'\n'+"date: "+date+'\n'+"time: "+time+'\n'+"vehical:SUV(6+1)"+'\n'+"AC:RS "+'\n'+"NON AC:RS ",# message
            # from mail
            'sarigecabs@gmail.com',
            
            ['sarigecabs@gmail.com'],# to mail
        )
    return render(request, 'email.html', {'name': name})
def sm4(request):

    if request.method == "POST":
        #send an email
        send_mail(

            name ,#subject
            "name: "+name+'\n'+"phone no: "+phone+'\n'+"pick: "+pick+'\n'+"drope: "+drop+'\n'+"car: "+car+'\n'+"date: "+date+'\n'+"time: "+time+'\n'+"vehical:SUV(7+1)"+'\n'+"AC:RS "+'\n'+"NON AC:RS ",# message
            # from mail
            'sarigecabs@gmail.com',
            
            ['sarigecabs@gmail.com'],# to mail
        )
    return render(request, 'email.html', {'name': name})
def sm5(request):
    if request.method == "POST":
        #send an email
        send_mail(

            name ,#subject
            "name: "+name+'\n'+"phone no: "+phone+'\n'+"pick: "+pick+'\n'+"drope: "+drop+'\n'+"car: "+car+'\n'+"date: "+date+'\n'+"time: "+time+'\n'+"vehical:T.T(18+1)"+'\n'+"AC:RS "+'\n'+"NON AC:RS ",# message
            # from mail
            'sarigecabs@gmail.com',
            
            ['sarigecabs@gmail.com'],# to mail
        )
    return render(request, 'email.html', {'name': name})
def sm6(request):
    if request.method == "POST":
        #send an email
        send_mail(

            name ,#subject
            "name: "+name+'\n'+"phone no: "+phone+'\n'+"pick: "+pick+'\n'+"drope: "+drop+'\n'+"car: "+car+'\n'+"date: "+date+'\n'+"time: "+time+'\n'+"vehical:MINI BUS(18+1)"+'\n'+"AC:RS "+'\n'+"NON AC:RS ",# message
            # from mail
            'sarigecabs@gmail.com',
            
            ['sarigecabs@gmail.com'],# to mail
        )
    return render(request, 'email.html', {'name': name})
def sm7(request):
    if request.method == "POST":
        #send an email
        send_mail(

            name ,#subject
            "name: "+name+'\n'+"phone no: "+phone+'\n'+"pick: "+pick+'\n'+"drope: "+drop+'\n'+"car: "+car+'\n'+"date: "+date+'\n'+"time: "+time+'\n'+"vehical:MINI BUS(21+1)"+'\n'+"AC:RS "+'\n'+"NON AC:RS ",# message
            # from mail
            'sarigecabs@gmail.com',
            
            ['sarigecabs@gmail.com'],# to mail
        )
    return render(request, 'email.html', {'name': name})
def sm8(request):
    if request.method == "POST":
        #send an email
        send_mail(

            name ,#subject
            "name: "+name+'\n'+"phone no: "+phone+'\n'+"pick: "+pick+'\n'+"drope: "+drop+'\n'+"car: "+car+'\n'+"date: "+date+'\n'+"time: "+time+'\n'+"vehical:MINI BUS (25+1)"+'\n'+"AC:RS "+'\n'+"NON AC:RS ",# message
            # from mail
            'sarigecabs@gmail.com',
            
            ['sarigecabs@gmail.com'],# to mail
        )
    return render(request, 'email.html', {'name': name})
def sm9(request):
    if request.method == "POST":
        #send an email
        send_mail(

            name ,#subject
            "name: "+name+'\n'+"phone no: "+phone+'\n'+"pick: "+pick+'\n'+"drope: "+drop+'\n'+"car: "+car+'\n'+"date: "+date+'\n'+"time: "+time+'\n'+"vehical:BUS(33+1)"+'\n'+"AC:RS "+'\n'+"NON AC:RS ",# message
            # from mail
            'sarigecabs@gmail.com',
            
            ['sarigecabs@gmail.com'],# to mail
        )
    return render(request, 'email.html', {'name': name})
def sm10(request):
    if request.method == "POST":
        #send an email
        send_mail(

            name ,#subject
            "name: "+name+'\n'+"phone no: "+phone+'\n'+"pick: "+pick+'\n'+"drope: "+drop+'\n'+"car: "+car+'\n'+"date: "+date+'\n'+"time: "+time+'\n'+"vehical:BUS(40+1)"+'\n'+"AC:RS "+'\n'+"NON AC:RS ",# message
            # from mail
            'sarigecabs@gmail.com',
            
            ['sarigecabs@gmail.com'],# to mail
        )
    return render(request, 'email.html', {'name': name})
def sm11(request):
    if request.method == "POST":
  
        #send an email
        send_mail(

            name ,#subject
            "name: "+name+'\n'+"phone no: "+phone+'\n'+"pick: "+pick+'\n'+"drope: "+drop+'\n'+"car: "+car+'\n'+"date: "+date+'\n'+"time: "+time+'\n'+"vehical:BUS(50+1)"+'\n'+"AC:RS "+'\n'+"NON AC:RS ",# message
            # from mail
            'sarigecabs@gmail.com',
            
            ['sarigecabs@gmail.com'],# to mail
        )
    return render(request, 'email.html', {'name': name})
    

def elements(request):
    return render(request, 'elements.html')

def news(request):
    return render(request, 'index.html')

def tbl(request):
    return render(request, 'tbl.html')

def email(request):
    return render(request, 'email.html')

def honey(request):
    return render(request, 'honeymoon.html')

def outstion(request):
    return render(request, 'outstion.html')

def tour(request):
    return render(request, 'tour.html')

def airport(request):
    if request.method == "POST":
        global name
        global phone
        global pick
        global drop
        global drop
        global car
        global date
        global time
        global airport
        global toarpt
        
    
        name = request.POST['nm']
        phone = request.POST['em']
        pick = request.POST['ph']
        drop = request.POST['pi']
        car = request.POST['dr']
        date = request.POST['tm']
        time = request.POST['dt']
        
    
        #send an email

        return render(request, 'airport.html', {'name': name})
        
    else:
        return render(request, 'airport.html')
    return render(request, 'airport.html')
