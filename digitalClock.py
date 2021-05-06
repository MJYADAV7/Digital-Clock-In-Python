from tkinter import *
import time

def clock():
    now=time.strftime("%H:%M:%S")
    label1=Label(root,font= 'DS-Digital 100 ', bg="black", fg="blue",text=now)
    label1.after(200,clock)
    label1.grid(row=0,column=1)
root=Tk()
root.title("Digital Clock")
root.resizable(False,False)
clock()
root.mainloop()
