from django.shortcuts import render
from django.http import JsonResponse
from shop.models import Product, Order, OrderUpdate
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

def man(request):
    return render(request, 'shop/man.html')

def woman(request):
    return render(request, 'shop/woman.html')

def thankyou(request):
    return render(request, 'shop/thankyou.html')

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
def sentemail1(request):
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

@csrf_exempt
def tracker(request):
    if request.method == 'POST':
        params = json.loads(request.body)
        print(params['orderId'])
        print(params['email'])
        try:
            order = Order.objects.filter(order_id=params['orderId'], email=params['email'])
            print(order)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=params['orderId'])
                # print(update)
                payload = list(update.values())
                return JsonResponse({'err':'false', 'message' : 'Order Tracked', 'payload' : payload})
            else:
                return JsonResponse({'err':'true', 'message' : 'Please Enter Right Order Id or Email'})
        except Exception as e:
            # print(e)
            return JsonResponse({'err':'true', 'message' : 'Something West Worng'})
    return render(request, 'shop/tracker.html')

def search(request):
    return JsonResponse({'message' : 'This is search page'})

@csrf_exempt
def cheackout(request):
    if request.method == 'POST':
        params = json.loads(request.body)
        print(params['ordered_item'])
        address = f"{params['addressLine1']} - {params['addressLine2']}"
        order = Order(first_name=params['first_name'], last_name=params['last_name'], email=params['email'], phone=params['phone'], address=address, 
                        city=params['city'], state=params['state'], zip_code=params['zip_code'], ordered_item=params['ordered_item'])
        order.save()
        print(order.order_id)
        order_id = order.order_id
        update = OrderUpdate(order_id=order_id, update_desc="Order Placed", status="Order Placed")
        update.save()
        sentMail(order_id,params['email'])
        return JsonResponse({'err': 'false', 'message' : 'Order Placeed', 'order_id': order_id})

def sentMail(order_id, email):
    # emailArr = []
    # emailArr.append(email)
    email = EmailMessage(subject = 'Order Confirmed',
                                body = f'Your Order succesfully placed. Your order Id {order_id}',
                                from_email = 'Cart Shart',
                                to = [email])
    email.send()
    return True