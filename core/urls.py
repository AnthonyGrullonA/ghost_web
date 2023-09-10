from django.contrib import admin
from django.urls import path
from website import views as ws

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ws.index, name='index'),
]
