from django.contrib import admin
from django.urls import path
from website import views as ws

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ws.index, name='index'),
    path('about/', ws.About, name='about'),
    path('blog/', ws.Blog, name='blog'),
    path('contact/', ws.Contact, name='contact'),
    path('portafolio/', ws.Portafolio, name='poortafolio'),
    path('pricing', ws.Pricing, name='pricing'),
    path('service/', ws.Service, name='service'),
    path('single-post/', ws.Single_Post, name='single post'),
    path('team/', ws.Team, name='Team'),
]
