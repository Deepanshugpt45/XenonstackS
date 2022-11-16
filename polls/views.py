from django.shortcuts import render
from polls.models import savedata_contact

# Create your views here.
def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')


def savedata_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        en=savedata_contact(name=name,email=email,phone=phone,message=message)
        en.save()
    return render(request,'Contact.html')