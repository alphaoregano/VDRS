from livecaresys import *
from tkinter import *
import pymysql
from multiprocessing.pool import ThreadPool
import threading, time, sys
##from notify import *

#root =Tk()

#root.wm_geometry("%dx%d+%d+%d" % (1000,200,40,20))

connection = pymysql.connect(host='localhost',database='vehicle',user='root',password='')
cursor = connection.cursor()

def get(vehicles):
      res=vehicles
      print(vehicles)
##    for i in range(len(res)):
##        if(len(res[i])>0):
##          for j in range(len(res[i])):
##              plate_no = res[i][0]
##              color = res[i][1]
##              make = res[i][2]
##              b_type = res[i][3]
##              model = res[i][4]
##              input_type='video-frame-vid5'
##              
##              x=(plate_no,color,make,b_type,model)
##              print(x)
##
##              query = """INSERT INTO crime_record(plate_no, color, make,body_type,model) 
##                             VALUES (%s,%s,%s,%s,%s) """
##
##              
##              cursor.execute(query,x)
##              connection.commit()

    
    

##    vlist = ['MH02123','B191TV','H01BF2348']

    #for i in range(len(vlist)):
##    sqlite_select_query = """SELECT * from crime_record"""
##    cursor.execute(sqlite_select_query)
##    records = cursor.fetchall()
##    
##    w=50
##
##    for i in range(len(vlist)):
##        x=vlist[i]
##        c=0
##        for j in range(len(records)):
##            if(records[j][2]==x):
##                print(vlist[i],"successfully located")
##                c=c+1
##                #get_response(records[j][2],records[j][3],records[j][4])
##                
##                x="Vehicle with number "+records[j][2]+" and color "+records[j][3]+" made by "+records[j][4]+" has been spotted at Nagpada Signal."
##                            
##                labela = Label(root, text ="Notification Page",font=(40), width=100,anchor='center')        
##                labela.place(x=10, y=10)
##            
##                labela = Label(root, text =x,font=(5))        
##                labela.place(x=10, y=w)  #for loop
##                w=w+40
##                        
##            if(c==1):
##                break
##            
##get()
    
threading.Thread(target = livecaresysfunc, args=("http://192.168.43.1:8080/stream.mjpeg",0,'call_live','get','in',)).start()


