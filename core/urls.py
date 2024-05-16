from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),No changes detected
    path('', views.index, name='index'),
    path('signup', views.signup, name ='signup'),

]