from django.shortcuts import render

# Create your views here.

def filters(request):
    d={'data':'hAi hOW ArE YoU'}
    return render(request,'filters.html',d)