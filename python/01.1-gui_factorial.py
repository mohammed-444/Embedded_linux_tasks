from tkinter import *
import math

def on_click():
    if len(e.get())!=0:
        result_l.config(text='The factorial of '+e.get()+' = '+str(math.factorial(int(e.get()))))

win = Tk()
win.title('factorial')
l = Label(win,text='Enter the number: ')
e = Entry(win,width=25)
result_l = Label(win)
button = Button(win,text='calculate factorial',width=25,command=on_click)

l.grid(row=2,column=2)
e.grid(row=2,column=3)
result_l.grid(row=3,column=3)
button.grid(row=4,column=3)


win.mainloop()