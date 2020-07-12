from flask import Flask, render_template
import pyodbc

import django

app = Flask(__name__)

i=1

conn = pyodbc.connect(
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\saurabh\Desktop\DATABASE.mdb;')
cursor = conn.cursor()
cursor.execute('select * from DATA1')

s1 = cursor.fetchall()

# for row in cursor.fetchall():
#    print(row)


tcode="""
<td class='c4'><a href="home" class='c3' >Design Document Generation</a></td>
<td class='c4'><a href="home" class='c3' >Layout Comparision</a></td>
<td class='c4'><a href="home" class='c3' >Cavity Comparision</a></td>
<td class='c4'><a href="home" class='c3' >Pattern Comparison</a></td>
"""

@app.route("/")

@app.route("/welcome")
def welcome():

    return render_template('welcome.html')


@app.route("/home")
def home():

    return render_template('home.html')

@app.route("/tes")
def tes():


    return render_template('tes.html', tcode=tcode, s1=s1, i=i)

if __name__ == "__main__":
    app.run(debug=True)