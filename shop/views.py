from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def shopHome(request):
    return render(request, 'shop/shopHome.html')

def about(request):
    return JsonResponse({'message' : 'this is about page'})

def contact(request):
    return JsonResponse({'message' : 'this is contact page'})

def productview(request):
    return render(request, 'shop/viewProduct.html')

def tracker(request):
    return JsonResponse({'message' : 'This is tracker page'})

def search(request):
    return JsonResponse({'message' : 'This is search page'})

def cheackout(request):
    return JsonResponse({'message' : 'This is cheackout page'})