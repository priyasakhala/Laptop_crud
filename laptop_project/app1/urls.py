from django.urls import  path
from . import  views

urlpatterns = [
    path('lv/',views.LaptopView, name='lapform_url'),
    path('sl/',views.ShowLaptopView, name='showlap_url'),
    path('ul/<int:id>/',views.UpdateLaptopView, name='updatelap_url'),
    path('dl/<int:id>/',views.DeleteLaptopView, name='deletelap_url')
]