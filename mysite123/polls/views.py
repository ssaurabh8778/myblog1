<<<<<<< HEAD
from django.shortcuts import render
import sqlite3
# Create your views here.
from django.shortcuts import render
import pyodbc

def index(request):
    return render(request,'polls/welcome.html')

conn = sqlite3.connect('/home/ssaurabh8778/ssaurabh8778.pythonanywhere.com/mysite123/polls/data.sqlite')
cursor = conn.cursor()
cursor.execute('')

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
=======
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import pyodbc

def index(request):
    return render(request,'polls/welcome.html')

conn = pyodbc.connect(
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=polls/DATABASE.mdb;')
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
>>>>>>> 97c628cb69f003a77bcc5e5d7b9cf7ad30d53317
