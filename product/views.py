from django.shortcuts import render
from django.http import HttpResponse
#function based
# Create your views here.
def welcome(request):
    return HttpResponse('Welcome Message')

def tatabye(requst):
    return HttpResponse('Tata byebye')

def list_product(request):
    return HttpResponse('Iron, Bulb, .....')

def list_product_price(request):
    return HttpResponse('1000: iron, 2000:bulb')

def product_add_with_html(request):
    data= {'name': "This is add product section"}
    return render(request,'product/add_product.html',data)

# request, html_filepath from basedir, context {}, 
{
    'key':'value',
    'key':'value',
    'key':'value',
    'key':'value',
    'key':'value',
    'key':['value'],
    
}