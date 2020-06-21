from django.shortcuts import render
from django.http import JsonResponse
from shop.models import Product
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail,EmailMessage
from django.core import serializers

# Create your views here.

def shopHome(request):
    return render(request, 'shop/shopHome.html')

def about(request):
    return JsonResponse({'message' : 'this is about page'})

def contact(request):
    return JsonResponse({'message' : 'this is contact page'})


def productview(request, id):
    return render(request, 'shop/viewProduct.html')

@csrf_exempt
def cart(request):
    if request.method == 'POST':
        params = json.loads(request.body)
        print(params)
        payload = []
        for item in params['ids']:
            data = Product.objects.filter(product_id=item)
            # payload.append(json.dumps(data.values()))
            payload.append(list(data.values()))
            # payload.append(serializers.serialize('json', data))
            # qs_json = serializers.serialize('json', data)
        print(payload)
        return JsonResponse({"err":"false", "message":"ok", 'data': payload})
    return render(request, 'shop/cart2.html')

def placeOrder(request):
    return render(request, 'shop/placeOrder.html')


@csrf_exempt
def product_view(request):
    if request.method == 'POST':
        params = json.loads(request.body)
        print(params['id'])
        data = Product.objects.filter(product_id=params['id'])
        # print(data.values())
        payload = list(data.values())
        return JsonResponse({'err' : 'false', 'message' : 'Fetched', 'data': payload})
    


@csrf_exempt
def allproduct(request):
    
    if request.method == 'POST':
        data = Product.objects.all()
        # print(data.values())
        payload = list(data.values())
        return JsonResponse({'err' : 'false', 'message' : 'Fetched', 'data': payload})
    # return render(request, 'shop/viewProduct.html')


@csrf_exempt
def sentemail(request):
    
    if request.method == 'POST':
        # res = send_mail(
        #     'Subject here',
        #     'Here is the message.',
        #     'shubhamroy12345@gmail.com',
        #     ['shubham.roy021@gmail.com'],
        #     fail_silently=False,
        # )
        # print(res)
        email = EmailMessage(subject = 'Order Confirmed',
                                body = 'Your Order succesfully placed',
                                from_email = 'Cart Shart',
                                to = ['shubham.roy021@gmail.com','codeingschool73@gmail.com'])
        email.send()
        print(email.message)
        return JsonResponse({'err' : 'false', 'message' : 'Fetched', 'data': 'payload'})
    # return render(request, 'shop/viewProduct.html')


def tracker(request):
    return JsonResponse({'message' : 'This is tracker page'})

def search(request):
    return JsonResponse({'message' : 'This is search page'})

def cheackout(request):
    return JsonResponse({'message' : 'This is cheackout page'})