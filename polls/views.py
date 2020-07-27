from django.shortcuts import render
import sqlite3
# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request,'polls/welcome.html')

conn = sqlite3.connect('/polls/data.sqlite')
cursor = conn.cursor()
cursor.execute('select * from DATA1')

s1 = cursor.fetchall()




def home(request):
    return render(request,'polls/home.html', {'s1' : s1})

def total_filled1(request):
    return render(request, 'polls/total_filled.html', {'s1' : s1})

def data_interface1(request):
    return render(request, 'polls/data_interface.html', {'s1' : s1})

def testing1(request):
    return render(request, 'polls/testing.html', {'s1' : s1})

def testing_data1(request):
    return render(request, 'polls/testing_data.html', {'s1' : s1})