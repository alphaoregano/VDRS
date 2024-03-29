from tkinter import *
import tkinter.font as font
from PIL import ImageTk, Image
import os
import image
import video
import text


sel= ''
global textbox1

root = Tk()
root.title("Vehicle Recognition And Detection System")
root.wm_geometry("%dx%d+%d+%d" % (1536,864,-7,0))

myfont =font.Font(family="Microsoft JhengHei UI Light")





def text():            
            def on_click1(event):
                #textbox1.configure(state=NORMAL)
                textbox1.delete(0, END)
                textbox1.unbind('<Button-1>', on_click_id1)
            def on_click2(event):
                textbox2.configure(state=NORMAL)
                textbox2.delete(0, END)
                textbox2.unbind('<Button-1>', on_click_id2)
            def on_click3(event):
                textbox3.configure(state=NORMAL)
                textbox3.delete(0, END)
                textbox3.unbind('<Button-1>', on_click_id3)
            def on_click4(event):
                textbox4.configure(state=NORMAL)
                textbox4.delete(0, END)
                textbox4.unbind('<Button-1>', on_click_id4)
            def on_click5(event):
                textbox5.configure(state=NORMAL)
                textbox5.delete(0, END)
                textbox5.unbind('<Button-1>', on_click_id5)
                
            textframe = Frame(root,height=540,width=450,highlightbackground="black", highlightthickness=0,bg="white").place(x=210, y=60)
            
            label1 = Label(textframe, text = "Text input",height=2,font=font.Font(family="Microsoft JhengHei UI Light",size=14),anchor='w',relief=FLAT,bg="white").place(x=290, y=124)
            textbox1 = Entry(textframe,font=myfont,relief=GROOVE,highlightbackground="black", highlightthickness=1)
            textbox1.insert(0, "Plate No")
            textbox1.configure(state=DISABLED)
            on_click_id1 = textbox1.bind('<Button-1>', on_click1)
            textbox1.place(x=250, y=184)

            textbox2 = Entry(textframe,font=myfont,relief=GROOVE,highlightbackground="black", highlightthickness=1)
            textbox2.insert(0, "Color")
            textbox2.configure(state=DISABLED)
            on_click_id2 = textbox2.bind('<Button-1>', on_click2)
            textbox2.place(x=250, y=234)

            textbox3 = Entry(textframe,font=myfont,relief=GROOVE,highlightbackground="black", highlightthickness=1)
            textbox3.insert(0, "Make")
            textbox3.configure(state=DISABLED)
            on_click_id3 = textbox3.bind('<Button-1>', on_click3)
            textbox3.place(x=250, y=284)

            textbox4 = Entry(textframe,font=myfont,relief=GROOVE,highlightbackground="black", highlightthickness=1)
            textbox4.insert(0, "Body Type")
            textbox4.configure(state=DISABLED)
            on_click_id4 = textbox4.bind('<Button-1>', on_click4)
            textbox4.place(x=250, y=334)

            textbox5 = Entry(textframe,font=myfont,relief=GROOVE,highlightbackground="black", highlightthickness=1)
            textbox5.insert(0, "Model")
            textbox5.configure(state=DISABLED)
            on_click_id5 = textbox5.bind('<Button-1>', on_click5)
            textbox5.place(x=250, y=384)

            add_Button = Button(textframe, text = "Submit",height=1,width=10,font=font.Font(family="Microsoft JhengHei UI Light",weight='bold'),bg="black",fg="white", command = lambda:text.textFeed(textbox1.get(),textbox2.get(),textbox3.get(),textbox4.get(),textbox5.get()))
            add_Button.place(x=285, y=450)

def imagei():
    imageframe = Frame(root,height=500,width=500,highlightbackground="gray", highlightthickness=0,bg="white").place(x=150, y=110)

    label1 = Label(imageframe, text = "Image file:",height=2,font=myfont,anchor='w',relief=FLAT,bg="white").place(x=210, y=150)
    textbox1 = Entry(imageframe,width=40,relief=GROOVE,highlightbackground="black", highlightthickness=1)
    textbox1.place(x=310, y=164)

    add_Button = Button(imageframe, text = "Browse",height=1,width=7,font=myfont, command = lambda:dia(textbox1),relief=FLAT,bg="white")
    add_Button.place(x=260, y=250)

    add_Button = Button(imageframe, text = "Submit",height=1,width=7,font=myfont, command = lambda:createi(),relief=FLAT,bg="white")
    add_Button.place(x=360, y=250)
    
def dia(text):
    name = image.fileDialog()
    text.delete(0,END)
    text.insert(0,name)
    global fname
    fname = name
    
def pro(name):
    image.process(name)
    
def createi():
    def curselect(event):
        global sel,lis
        widget = event.widget
        selection=widget.curselection()
        picked = widget.get(selection[0])
        #strpicked = picked.split(".....")
        sel = picked[0]
        for i in range(len(lis)):
            for j in range(len(lis[i])):
                if lis[i][j][0] == sel:
                    sel = lis[i][j]
                    
    selectframe = Frame(root,height=500,width=500,highlightbackground="gray", highlightthickness=0,bg="white").place(x=150, y=110)
    yax = 150
    global lis,fname,sel
    lis = image.detec(fname)
    label = Label(root, text = "Detected vehicles:",height=2,width=100,font=myfont,anchor='w',relief=FLAT,bg="white").place(x=205, y=yax-50)

    label = Label(selectframe, text = "Plate No",font=font.Font(family="Microsoft JhengHei UI Light",size=10),anchor='w',relief=FLAT,bg="white").place(x=170, y=180)
    label = Label(selectframe, text = "Color",font=font.Font(family="Microsoft JhengHei UI Light",size=10),anchor='w',relief=FLAT,bg="white").place(x=235, y=180)
    label = Label(selectframe, text = "Make",font=font.Font(family="Microsoft JhengHei UI Light",size=10),anchor='w',relief=FLAT,bg="white").place(x=290, y=180)
    label = Label(selectframe, text = "Body type",font=font.Font(family="Microsoft JhengHei UI Light",size=10),anchor='w',relief=FLAT,bg="white").place(x=355, y=180)
    label = Label(selectframe, text = "Model",font=font.Font(family="Microsoft JhengHei UI Light",size=10),anchor='w',relief=FLAT,bg="white").place(x=460, y=180)

    mylistbox=Listbox(selectframe,width=60,height=15,font=font.Font(family="Microsoft JhengHei UI Light",size=10))
    mylistbox.bind('<<ListboxSelect>>',curselect)
    mylistbox.place(x=170,y=200)
    add_Button = Button(selectframe, text = "Add",command=lambda :pro(sel),height=1,font=myfont,anchor='w',relief=FLAT,bg="white").place(x=400, y=160)
    
    for i in range(len(lis[-1])):
        #temp = lis[-1][i]
        mylistbox.insert(END,lis[-1][i])

    
        
        
        
def videoi():
    videoframe = Frame(root,height=500,width=500,highlightbackground="gray", highlightthickness=0,bg="white").place(x=150, y=110)

    label1 = Label(videoframe, text = "Video file:",height=2,width=100,font=myfont,anchor='w',relief=FLAT,bg="white").place(x=210, y=150)
    textbox1 = Entry(videoframe,width=40,relief=GROOVE,highlightbackground="black", highlightthickness=1)
    textbox1.place(x=310, y=164)

    add_Button = Button(videoframe, text = "Browse",height=1,width=7,font=myfont, command = lambda:dia(textbox1),relief=FLAT,bg="white")
    add_Button.place(x=260, y=250)

    add_Button = Button(videoframe, text = "Submit",height=1,width=7,font=myfont, command = lambda:createv(),relief=FLAT,bg="white")
    add_Button.place(x=360, y=250)
    
def createv():
    def curselect(event):
        global sel,lis
        widget = event.widget
        selection=widget.curselection()
        picked = widget.get(selection[0])
        #strpicked = picked.split(".....")
        sel = picked[0]
        for i in range(len(lis)):
            for j in range(len(lis[i])):
                if lis[i][j][0] == sel:
                    sel = lis[i][j]
                    
    selectframe = Frame(root,height=500,width=500,highlightbackground="gray", highlightthickness=0,bg="white").place(x=150, y=110)
    global lis,fname,sel
    lis = video.detec(fname)
    label = Label(selectframe, text = "Detected vehicles:",height=2,width=100,font=myfont,anchor='w',relief=FLAT,bg="white").place(x=205, y=100)

    label = Label(selectframe, text = "Plate No",font=font.Font(family="Microsoft JhengHei UI Light",size=10),anchor='w',relief=FLAT,bg="white").place(x=170, y=180)
    label = Label(selectframe, text = "Color",font=font.Font(family="Microsoft JhengHei UI Light",size=10),anchor='w',relief=FLAT,bg="white").place(x=235, y=180)
    label = Label(selectframe, text = "Make",font=font.Font(family="Microsoft JhengHei UI Light",size=10),anchor='w',relief=FLAT,bg="white").place(x=290, y=180)
    label = Label(selectframe, text = "Body type",font=font.Font(family="Microsoft JhengHei UI Light",size=10),anchor='w',relief=FLAT,bg="white").place(x=355, y=180)
    label = Label(selectframe, text = "Model",font=font.Font(family="Microsoft JhengHei UI Light",size=10),anchor='w',relief=FLAT,bg="white").place(x=460, y=180)

    mylistbox=Listbox(selectframe,width=60,height=15,font=font.Font(family="Microsoft JhengHei UI Light",size=10))
    mylistbox.bind('<<ListboxSelect>>',curselect)
    mylistbox.place(x=170,y=200)
    add_Button = Button(selectframe, text = "Add",command=lambda :pro(sel),height=1,font=myfont,anchor='w',relief=FLAT,bg="white").place(x=400, y=160)

    for i in range(len(lis)):
        for j in range(len(lis[i])):
            #temp = lis[i]
            mylistbox.insert(END, lis[i][j])   

    

def blist():
    blistframe = Frame(root,height=500,width=500,highlightbackground="gray", highlightthickness=0,bg='white').place(x=150, y=110)
    global lis,fname,sel
    lis = image.fetch()
    label = Label(blistframe, text = "BlackList",font=font.Font(family="Microsoft JhengHei UI Light",size=20),anchor='w',relief=FLAT,bg="white").place(x=300, y=120)
    
    label = Label(blistframe, text = "Plate No",font=font.Font(family="Microsoft JhengHei UI Light",size=10),anchor='w',relief=FLAT,bg="white").place(x=170, y=180)
    label = Label(blistframe, text = "Color",font=font.Font(family="Microsoft JhengHei UI Light",size=10),anchor='w',relief=FLAT,bg="white").place(x=235, y=180)
    label = Label(blistframe, text = "Make",font=font.Font(family="Microsoft JhengHei UI Light",size=10),anchor='w',relief=FLAT,bg="white").place(x=290, y=180)
    label = Label(blistframe, text = "Body type",font=font.Font(family="Microsoft JhengHei UI Light",size=10),anchor='w',relief=FLAT,bg="white").place(x=355, y=180)
    label = Label(blistframe, text = "Model",font=font.Font(family="Microsoft JhengHei UI Light",size=10),anchor='w',relief=FLAT,bg="white").place(x=460, y=180)
    
    mylistbox=Listbox(blistframe,width=60,height=15,font=font.Font(family="Microsoft JhengHei UI Light",size=10))
    #mylistbox.bind('<<ListboxSelect>>',curselect)
    mylistbox.place(x=170,y=200)

    for i in range(len(lis)):
            mylistbox.insert(END, lis[i])   
    
img = Image.open(r"G:\Usaid-Projects\SIH\logo.png")
img = img.resize((60,60), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

headfr = Frame(root,height=60,width=1400,highlightbackground="black", highlightthickness=0,background='black').place(x=210, y=0)

sidefr = Frame(root,height=600,width=210,background='white',highlightbackground="black", highlightthickness=0,bg='#717171').place(x=0, y=0)

panel = Label(headfr,height=60,width=60,image = img,bg='#717171').place(x=10, y=10)

labela = Label(sidefr, text = "VDRS",font=font.Font(family="Microsoft JhengHei UI Light",size=20,),anchor='center',bg='#717171').place(x=70, y=10)
labela = Label(sidefr, text = "Recognition System",font=font.Font(family="Microsoft JhengHei UI Light",size=10),anchor='center',bg='#717171').place(x=70, y=63)
labela = Label(sidefr, text = "Vehicle Detection And",font=font.Font(family="Microsoft JhengHei UI Light",size=10),anchor='center',bg='#717171').place(x=70, y=45)

add_Button = Button(sidefr, text = "Text Details",command=text,height=1,width=23,font=myfont,anchor='center',bg='white',fg="black",relief=FLAT).place(x=0, y=120)

add_Button = Button(sidefr, text = "Image Details", command = imagei,height=1,width=23,font=myfont,anchor='center',bg='white',fg="black",relief=FLAT).place(x=0, y=170)

add_Button = Button(sidefr, text = "Video Details", command = videoi, height=1,width=23,font=myfont,anchor='center',bg='white',fg="black",relief=FLAT).place(x=0, y=230)

add_Button = Button(sidefr, text = "BlackList", command = blist, height=1,width=11,font=myfont,anchor='center',bg='white',fg="black",relief=FLAT).place(x=230, y=10)

text()































