from tkinter import filedialog
from tkinter import *
import pymysql
import mysql.connector
from tkinter import messagebox
from mysql.connector import Error
from mysql.connector import errorcode
from caresys import *

connection = pymysql.connect(host='localhost',database='vehicle',user='root',password='')

cursor = connection.cursor()

def detec(name):
     res = caresysfunc(0,name,0,'us')
     return res


def process(x):
     plate_no = x[0]
     color = x[1]
     make = x[5]
     b_type = x[3]
     model = x[4]
         
     x=(plate_no,color,make,b_type,model)
     query = """INSERT INTO crime_record(plate_no, color, make,body_type,model) 
                        VALUES (%s,%s,%s,%s,%s) """
     cursor.execute(query,x)
     connection.commit()
     messagebox.showinfo("Success!","Inserted "+ str(x) +" into blacklist")

     
def fileDialog():     
     filename = filedialog.askopenfilename(title = "Select A File")
     return filename
    
def fetch():
     cursor.execute("SELECT * FROM crime_record")
     rows = cursor.fetchall()
     return (rows)

