
from django.shortcuts import HttpResponse, render

from.models import Product,ContactForm

# Create your views here.



def home(request):
     
     products = Product.objects.filter(interestedFruit=True)
     return render(request,"home.html",{
          "products":products
     })

def about(request):
     return render(request,"about.html")


def contact(request):
     if request.method == 'POST':
          customerName=request.POST['customerName']
          phoneNumber=request.POST['phoneNumber']
          eMail=request.POST['eMail']
          mesagge=request.POST['mesagge']

          p=ContactForm(name=customerName, telephone=phoneNumber, email=eMail, mesagges=mesagge)
          p.save()
          print(customerName)
     return render(request,"contact.html")



def vegetables(request):
     products = Product.objects.filter(stockStatus=True)
     return render(request,"vegetables.html",{
          "products":products
     })