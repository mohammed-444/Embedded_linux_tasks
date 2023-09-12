# Write a program that make led on or off
from tkinter import *

def on_click_on():
    c.itemconfig(ovel,fill = 'red')
    result_l.config(text='Led is ON')

def on_click_off():
    c.itemconfig(ovel,fill = 'white')
    result_l.config(text='Led is OFF')

def on_click_blue():
    c.itemconfig(ovel,fill = 'blue')
    result_l.config(text='Led is blue')


win = Tk()
win.title('led control')
result_l = Label(win)
button_on = Button(win,text='Led On',width=25,command=on_click_on)
button_off = Button(win,text='Led OFF',width=25,command=on_click_off)
button_blue = Button(win,text='blue led',width=25,command=on_click_blue)
c= Canvas(win,width=400, height=400)


#Draw an Oval in the canvas
ovel = c.create_oval(60,60,210,210,fill='white')

c.grid(row=2,column=2)
result_l.grid(row=4,column=2)
button_on.grid(row=5,column=2)
button_off.grid(row=6,column=2)
button_blue.grid(row=7,column=2)
win.mainloop()