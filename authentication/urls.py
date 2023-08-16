from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('newapp', views.newapp, name='newapp'),
    path('vs', views.vs, name='vs'),
    path('view1', views.view1, name='view1'),
    path('charts', views.charts, name='charts'),
    path('index1', views.index1, name='index1'),
    path('tables', views.tables, name='tables'),
    path('approve', views.approve, name='approve'),
    path('gen', views.gen, name='gen'),
    path('s401', views.s401, name='s401'),
    path('s404', views.s404, name='s404'),
    path('s500', views.s500, name='s500'),
    path('index2', views.index2, name='index2'),
    path('charts2', views.charts2, name='charts2'),
    path('tables2', views.tables2, name='tables2'),
    path('approve2', views.approve2, name='approve2'),
    path('gen2', views.gen2, name='gen2'),
    path('s4012', views.s4012, name='s4012'),
    path('s4042', views.s4042, name='s4042'),
    path('s5002', views.s5002, name='s5002'),
]