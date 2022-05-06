from tkinter import *

def click(event):
    global scvalue

    text = event.widget.cget("text")

    if(text=="="):
        if scvalue.get().isdigit():
            value= int(scvalue.get())
        else:
            try:
                value= eval(screen.get())
                scvalue.set(value)
                screen.update()
            except Exception:
                scvalue.set("Error")
                screen.update()
    elif(text == "C"):
        scvalue.set("")
        screen.update()

    elif(text =="DEL"):
        scvalue.set(scvalue.get()[0:len(scvalue.get())-1])
        screen.update()

    else:
        scvalue.set(scvalue.get()+text)
        screen.update()
        
    
root = Tk()
root.geometry('500x800')
root.title("Calculator")
scvalue = StringVar()
scvalue.set("")
screen = Entry(root,textvar = scvalue,font = "Arial 36")
screen.pack()

f1 = Frame(root)
b1 = Button(f1,text ="C",font = "Arial 30")
b2 = Button(f1,text ="%",font = "Arial 30")
b3 = Button(f1,text ="DEL",font = "Arial 30")
bx = Button(f1,text ="/",font = "Arial 30")
b1.grid(row =2,column = 1)
b1.bind("<Button-1>",click)
b2.grid(row =2,column = 2)
b2.bind("<Button-1>",click)
b3.grid(row =2,column = 3)
b3.bind("<Button-1>",click)
bx.grid(row =2,column = 4)
bx.bind("<Button-1>",click)
f1.pack()

f2 = Frame(root)
b4 = Button(f2,text ="7",font = "Arial 30")
b5 = Button(f2,text ="8",font = "Arial 30")
b6 = Button(f2,text ="9",font = "Arial 30")
by = Button(f2,text ="*",font = "Arial 30")
b4.grid(row =3,column = 1)
b4.bind("<Button-1>",click)
b5.grid(row =3,column = 2)
b5.bind("<Button-1>",click)
b6.grid(row =3,column = 3)
b6.bind("<Button-1>",click)
by.grid(row =3,column = 4)
by.bind("<Button-1>",click)
f2.pack()

f3 = Frame(root)
b7 = Button(f3,text ="4",font = "Arial 30")
b8 = Button(f3,text ="5",font = "Arial 30")
b9 = Button(f3,text ="6",font = "Arial 30")
bz = Button(f3,text ="-",font = "Arial 30")
b7.grid(row =4,column = 1)
b7.bind("<Button-1>",click)
b8.grid(row =4,column = 2) 
b8.bind("<Button-1>",click)
b9.grid(row =4,column = 3)
b9.bind("<Button-1>",click)
bz.grid(row =4,column = 4)
bz.bind("<Button-1>",click)
f3.pack()

f4= Frame(root)
b7 = Button(f4,text ="3",font = "Arial 30")
b8 = Button(f4,text ="2",font = "Arial 30")
b9 = Button(f4,text ="1",font = "Arial 30")
bj = Button(f4,text ="+",font = "Arial 30")
b7.grid(row =5,column = 1)
b7.bind("<Button-1>",click)
b8.grid(row =5,column = 2)
b8.bind("<Button-1>",click)
b9.grid(row =5,column = 3)
b9.bind("<Button-1>",click)
bj.grid(row =5,column = 4)
bj.bind("<Button-1>",click)
f4.pack()

f5= Frame(root)
b10 = Button(f5,text ="0",font = "Arial 30")
b11 = Button(f5,text ="00",font = "Arial 30")
b12 = Button(f5,text =".",font = "Arial 30")
bk = Button(f5,text ="=",font = "Arial 30")
b10.grid(row =1,column = 1)
b10.bind("<Button-1>",click)
b11.grid(row =1,column = 2)
b11.bind("<Button-1>",click)
b12.grid(row =1,column = 3)
b12.bind("<Button-1>",click)
bk.grid(row =1,column = 3)
bk.bind("<Button-1>",click)
f5.pack()


root.mainloop()
