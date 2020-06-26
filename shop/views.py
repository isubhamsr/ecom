from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from shop.models import Product, Order, OrderUpdate, ContactUs
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail,EmailMessage
from django.core import serializers
from django.template.loader import get_template, render_to_string
from django.template import Context
import pdfkit
from xhtml2pdf import pisa
from io import BytesIO
import os
from tempfile import NamedTemporaryFile
from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator
from InvoiceGenerator.pdf import SimpleInvoice
from django.utils.html import strip_tags
from django.core import mail
# Create your views here.

def shopHome(request):
    return render(request, 'shop/shopHome.html')

def about(request):
    return render(request, 'shop/about.html')

def team(request):
    return render(request, 'shop/team.html')

@csrf_exempt
def contact(request):
    if request.method == "POST":
        params = json.loads(request.body)
        print(params)
        contact = ContactUs(name=params['name'], email=params['email'], message=params['message'])
        contact.save()
        return JsonResponse({'err': 'false', 'message': 'Message Send'})
    return render(request, 'shop/contactus.html')


def productview(request, id):
    return render(request, 'shop/viewProduct.html')

@csrf_exempt
def man(request):
    if request.method == "POST":
        params = json.loads(request.body)
        data = Product.objects.filter(category=params['category'])
        payload = list(data.values())
        # print(payload)
        return JsonResponse({'err':'false', 'message': 'Fetched', 'data' : payload})
    return render(request, 'shop/man.html')

@csrf_exempt
def woman(request):
    if request.method == "POST":
        params = json.loads(request.body)
        data = Product.objects.filter(category=params['category'])
        payload = list(data.values())
        # print(payload)
        return JsonResponse({'err':'false', 'message': 'Fetched', 'data' : payload})
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
        # print(payload)
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

def gen_pdf(request):
    # pdf = render_to_pdf('shop/pdf_template.html', {"data" :"Subham"})
    # response = HttpResponse(pdf, content_type='application/pdf')
    # filename = "output.pdf"
    # content = "attachment; filename=output.pdf" 
    # response['Content-Disposition'] = content
    # return response


# choose english as language
    os.environ["INVOICE_LANG"] = "en"

    client = Client('Client company')
    provider = Provider('My company', bank_account='2600420569', bank_code='2010')
    creator = Creator('John Doe')

    invoice = Invoice(client, provider, creator)
    invoice.currency_locale = 'en_US.UTF-8'
    invoice.add_item(Item(32, 600, description="Item 1"))
    invoice.add_item(Item(60, 50, description="Item 2", tax=21))
    invoice.add_item(Item(50, 60, description="Item 3", tax=0))
    invoice.add_item(Item(5, 600, description="Item 4", tax=15))
    pdf = SimpleInvoice(invoice)
    pdf.gen("invoice.pdf", generate_qr_code=True)
    return JsonResponse({'message' : 'This is search page'})

def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

@csrf_exempt
def cheackout(request):
    if request.method == 'POST':
        params = json.loads(request.body)
        print(type( params['ordered_item']))
        dict2 = params['ordered_item']
        address = f"{params['addressLine1']} - {params['addressLine2']}"
        totalPrice = 0
        print(type(dict2))
        for key in dict2:
            for another_key in dict2[key]:
            #print(another_key)
                if(another_key=="totalPrice"):
                    totalPrice=totalPrice+dict2[key][another_key]
        print(totalPrice)
        order = Order(first_name=params['first_name'], last_name=params['last_name'], email=params['email'], phone=params['phone'], address=address, 
                        city=params['city'], state=params['state'], zip_code=params['zip_code'],total_price=totalPrice,date=params['date'], ordered_item=params['ordered_item'])
        order.save()
        print(order.order_id)
        order_id = order.order_id
        update = OrderUpdate(order_id=order_id, update_desc="Order Placed", status="Order Placed")
        update.save()
        sentMail(order_id,params['email'], params['first_name'], params['last_name'], address, dict2, totalPrice, params['date'])
        return JsonResponse({'err': 'false', 'message' : 'Order Placeed', 'order_id': order_id})

def sentMail(order_id, email, first_name, last_name, address, orderItem, totalPrice, date):
    # emailArr = []
    # emailArr.append(email) 
    # for key, val in dict2.items():
    # if isinstance(val, dict):
    #     print(val.get('product_name'))
    #     print(val.get('quantity'))
    #     print(val.get('price'))
    #     print(val.get('totalPrice'))
    print(orderItem)
    subject = 'Order Confirmed'
    html_message = render_to_string('shop/mail_template.html', {'orderid': order_id, 'email' : email, 'first_name':first_name, 'last_name':last_name, 'address':address, 'orderItem': orderItem, 'totalPrice': totalPrice, 'date':date})
    plain_message = strip_tags(html_message)
    from_email = 'Cart Shart'
    to = email
    mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
    # email = EmailMessage(subject = 'Order Confirmed',
    #                             body = f'Your Order succesfully placed. Your order Id {order_id}',
    #                             from_email = 'Cart Shart',
    #                             to = [email])
    # email = EmailMessage(subject,plain_message,from_email,[to], html_message=html_message)
    # email.send()
    return True