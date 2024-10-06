from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def index(request):
#     return HttpResponse('this is my first file')

    
# def specfic(request):
#     number= 9731187318
#     return HttpResponse(number)

# def article(request,article_id):
#     return render(request,'myapp/home.html',{ 'article_id':article_id})

def index(request):
    return render(request,'myapp/home.html')

def getResponce(request):
    userMessage = request.GET.get('userMessage')
    return HttpResponse(userMessage)

from django.http import JsonResponse

def get_response(request):
    user_message = request.GET.get('userMessage', '')
    # Generate a response based on user_message
    bot_response = f": {user_message}"
    return JsonResponse({'response': bot_response})

