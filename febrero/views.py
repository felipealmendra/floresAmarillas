from django.shortcuts import render





def index(request):
    return render(request,"index.html")

def flores(request):
    return render(request,"flores.html")