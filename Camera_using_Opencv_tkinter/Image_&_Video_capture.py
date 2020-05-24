# -*- coding: utf-8 -*-
"""
Created on Fri May 22 11:43:32 2020

@author: KapilMangla
"""

import cv2 as cv
from tkinter import *
from PIL import Image, ImageTk
import datetime



#Function to display Frames on Tkinter  UI
def videost():
    ret,frame = cap.read()
    img=cv.cvtColor(frame ,cv.COLOR_BGR2RGB)
    img=Image.fromarray(img)
    imgtk=ImageTk.PhotoImage(img,master=root)
    Label1.imgtk=imgtk
    Label1.configure(image=imgtk)
    Label1.after(2, videost)


#Function to record video
def record():
    r,f=cap.read()
    if r==True:
        out.write(f)
        root.after_idle(record)
    
#Function to use video button for both start and stop recording    
def video_rec():
    
    global out
    
    datet=str(datetime.datetime.now())
    date=datet.split(".")
    date=date[0].replace("-","")
    date=date.replace(":","")
    date=date.replace(" ","")
    
    x=video_var.get()
    if(x == 'Start Recording'):
        
        out=cv.VideoWriter(f'VID{date}.avi', fourcc, 20, (640,480)) 
        video_var.set("Stop")
        record()
       
    else: 
        out.release()
        t="Start Recording"
        video_var.set(t)
        
    
        
#Function to capture image     
def capture():
    r,f=cap.read()
    cv.imwrite(f"{Label1['image']}.jpg",f)
        

    
    
 

fourcc=cv.VideoWriter_fourcc(*'XVID') 



#Code for UI
root=Tk()

root.geometry("840x580")
root.minsize(840,580)
root.maxsize(840,580)
root.configure(bg="powder blue")

l1=Label(root,text="Audio and Video Capture using Opencv & Tkinter",bg="red",font="comicsansms 15 bold", borderwidth=5, relief=SUNKEN)
l1.pack(pady=5,fill=X)
l2=Label(root,text="By -- Kapil Mangla",font="comicsanms 10 bold",bg="powder blue")
l2.pack()
Label1=Label(root,bg="powder blue")
Label1.place(x=0,y=70,width=840,height=380)

cap=cv.VideoCapture(0)


    
#Button for image capture
Cap_button=Button(root, text="Capture Image",command=capture).place(x=200,y= 470)

#Button for video capture
video_var=StringVar()
video_button=Button(root,textvariable=video_var,command= video_rec).place(x=600,y= 470)    
video_var.set("Start Recording")
videost()  


 
root.mainloop()  
cap.release() 
cv.destroyAllWindows()
    