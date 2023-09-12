from tkinter import *

def on_click():
    if(v.get() == 1):   
        result_l.config(text='The sub of M - N : '+em.get()+' - '+en.get()+' = '+str(int(em.get())-int(en.get())))
    elif(v.get() == 2):
        result_l.config(text='The sum of M + N : '+em.get()+' + '+en.get()+' = '+str(int(em.get())+int(en.get())))

    
win = Tk()
win.title('simple calculator')
labelM = Label(win,text='Enter the first number: ')
labelN = Label(win,text='Enter the the second number : ')
result_l = Label(win)
em = Entry(win)
en = Entry(win)
button = Button(win,text='calculate',width=25,command=on_click)

v = IntVar()
Radiobutton(win, text='sub',variable=v,value=1).grid(row=3,column=1)
Radiobutton(win, text='sum',variable=v,value=2).grid(row=4,column=1)
labelM.grid(row=1,column=1)
labelN.grid(row=2,column=1)
em.grid(row=1,column=2)
en.grid(row=2,column=2)

result_l.grid(row=3,column=2)
button.grid(row=4,column=2)
win.mainloop()