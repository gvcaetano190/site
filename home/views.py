from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def home(request):
    # context = {'mensagem': messages.success(request=request, message='Esta é uma mensagem de sucesso!')}
    return render(request, "index.html")