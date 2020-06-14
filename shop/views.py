from django.shortcuts import render
from django.http import JsonResponse
from shop.models import Product
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def shopHome(request):
    return render(request, 'shop/shopHome.html')

def about(request):
    return JsonResponse({'message' : 'this is about page'})

def contact(request):
    return JsonResponse({'message' : 'this is contact page'})

@csrf_exempt
def productview(request):
    if request.method == 'POST':
        data = Product.objects.all()
        # print(data.values())
        payload = list(data.values())
        return JsonResponse({'err' : 'false', 'message' : 'Fetched', 'data': payload})
    return render(request, 'shop/viewProduct.html')

def tracker(request):
    return JsonResponse({'message' : 'This is tracker page'})

def search(request):
    return JsonResponse({'message' : 'This is search page'})

def cheackout(request):
    return JsonResponse({'message' : 'This is cheackout page'})