from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'website/index.html')

def About(request):
    return render(request, 'website/about.html')

def Blog (request):
    return render(request, 'website/blog.html')

def Contact(request):
    return render(request, 'website/contact.html')

def Portafolio(request):
    return render(request, 'website/portafolio.html')

def Pricing(request):
    return render(request, 'website/pricing.html')

def Service(request):
    return render(request, 'website/servivce.html')

def Single_Post(request):
    return render(request, 'website/single-post.html')

def Team(request):
    return render(request, 'website/team.html')


