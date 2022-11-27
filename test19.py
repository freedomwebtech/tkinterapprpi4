from tkinter import*
import cv2
from PIL import Image, ImageTk,ImageDraw
import face_recognition
from datetime import datetime
import glob
import os
cap=cv2.VideoCapture(0)
images=[]
names=[]


   


def data():
    path = "/home/pi/mycode/images/*.*"
    for file in glob.glob(path):
        image = cv2.imread(file)
        a=os.path.basename(file)
        b=os.path.splitext(a)[0]
        names.append(b)
        images.append(image)
        print(names)

def snapshot():
    face_locations = face_recognition.face_locations(image1)
    for face_location in face_locations:
        top, right, bottom, left = face_location
        face_image = image1[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        pil_image.show()
        name=name_var.get()
        pil_image.save('/home/pi/mycode/images/'+name+'.jpg')

window=Tk()
window.geometry("700x840")
window.configure(bg='black')
name_var=StringVar()
Label(window,text="FREEDOMWEBTECH",font=("times new roman",30,"bold"),bg="black",fg="red").pack()
f1=LabelFrame(window,bg="red")
f1.pack()
l1=Label(f1)
l1.pack()


l2=Entry(f1,textvariable = name_var, font=('calibre',10,'normal')).pack()
Button(window,text="snapshot",command=snapshot,font=("times new roman",20,"bold"),bg="black",fg="red").pack()
Button(window,text = 'Update',command=data).pack()
#Button(window,text = 'facedetect',command=facedetect).pack()
while True:
    frame = cap.read()
    image1=cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
    pil_image1=Image.fromarray(image1)
    image=ImageTk.PhotoImage(pil_image1)
    l1['image']=image
    
    window.update()     
cap.release()    
