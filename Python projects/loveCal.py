from tkinter import *
from functools import *
from tkinter import messagebox
root=Tk()
root.iconbitmap("E:/mca/1Apython/project/GUI love calculator/love.ico")
name1=Label(root,text="Enter your name").grid(row=0,column=0)
v1=StringVar()
entry1=Entry(root,textvariable=v1).grid(row=0,column=1)
name2=Label(root,text="Enter your crush name").grid(row=1,column=0)
v2=StringVar()
entry2=Entry(root,textvariable=v2).grid(row=1,column=1)
labelresult=Label(root).grid(row=3,column=1)

def cal(v1,v2):
    e1=v1.get()
    e2=v2.get()
    sum=0
    for i in e1:
        for j in e2:
            sum+=ord(i)-ord(j)
    if sum<0:
        sum=-sum
    if sum>100:
        sum=100
    if len(e1)==0 or len(e2)==0:
        messagebox.showinfo("","Please provide both the names")
    if len(e1)>10 or len(e2)>10:
        messagebox.showinfo("","Please enter only first name")
    else:
        messagebox.showinfo("Love Calculator","Percentage "
                                                "is "+
                        str(sum)
                        +" %")
    return

par=partial(cal,v1,v2)
btn=Button(root,text="Submit",command=par).grid(row=2,column=1)

root.mainloop()
