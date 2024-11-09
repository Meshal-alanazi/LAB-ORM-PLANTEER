from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from plants.models import Plant
from .models import Contact

# Create your views here.



def plants_view(request:HttpRequest):

    return render(request,"main/plants_all.html")

def contact_view(request: HttpRequest):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact = Contact(
            first_name=first_name,
            last_name=last_name,
            email=email,
            message=message
        )
        contact.save()
        return redirect('main:Messages_view')

    return render(request, "main/contact.html")


def Messages_view(request: HttpRequest):
    contact = Contact.objects.all()
    return render(request, 'main/message.html', context={'contact': contact})