# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 21:45:14 2021

@author: nobin
"""
import boto3
from tkinter import *
from PIL import ImageTk
import PIL.Image
def output():
     with open(str(d_id.get()), 'rb') as document:
            img = bytearray(document.read())
            response = client.detect_document_text(Document={'Bytes': img})
            x=''
            for item in response["Blocks"]:
                if item["BlockType"] == "WORD":
                    x=x+item["Text"] + ' '
     t=Text(window,bg='white',fg='black',font='Helvetica 15 bold',width=60,height=6)
     t.insert(END, x)
     t.place(x=10,y=200)
client = boto3.client('textract')
window=Tk()
window.geometry('600x420')
window.title("OCR App")
im1 = PIL.Image.open("bg1.jpeg")
im=im1.resize((600,420))
ph = ImageTk.PhotoImage(im)
background_label =Label(window, image=ph).place(x=0, y=0, relwidth=1, relheight=1)
Label(window, text='DIGITRAN SOLUTIONS OCR APP',font='Helvetica 18 bold',bg='white').grid(row=0,column=0)
window.columnconfigure(0, weight=1)
clicked=StringVar()
d_id=StringVar()

Label(window,text='Enter the path of the document',bg='white').place(x=10,y=30)
idbox=Entry(window,textvariable = d_id, font=('calibre',10,'normal'),width=30).place(x=10,y=50)
Select=Button(window,text='Submit',bg='black',command=output,fg='white').place(x=150,y=100)
window.mainloop()