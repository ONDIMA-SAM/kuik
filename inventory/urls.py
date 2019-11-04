from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('assign/<serial_number>', views.assign,name='assign'),
    path('order/', views.order, name='order'),
]
