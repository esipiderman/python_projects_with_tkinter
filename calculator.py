#calculator
from tkinter import *

def btnClick(number):
    global operator
    operator=operator +str(number)
    text_input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_input.set("")

def btnEqualInput():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=""

cal=Tk()
cal.title("calculator")
operator=""
text_input=StringVar()
textdisplay=Entry(cal,font=('arial',20,'bold'),bg="powder blue",foreground="black",textvariable=text_input,bd=30,insertwidth=4,justify='right').grid(columnspan=4)
#first row
btn7 = Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text="7",command=lambda:btnClick(7)).grid(row=1,column=0)
btn8= Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text="8",command=lambda:btnClick(8)).grid(row=1,column=1)
btn9= Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text="9",command=lambda:btnClick(9)).grid(row=1,column=2)
addition= Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text="+",command=lambda:btnClick('+')).grid(row=1,column=3)
#second row
btn4 = Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text="4",command=lambda:btnClick(4)).grid(row=2,column=0)
btn5 = Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text="5",command=lambda:btnClick(5)).grid(row=2,column=1)
btn6 = Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text="6",command=lambda:btnClick(6)).grid(row=2,column=2)
subtraction = Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text="-",command=lambda:btnClick('-')).grid(row=2,column=3)
#third row
btn1 = Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text="1",command=lambda:btnClick(1)).grid(row=3,column=0)
btn2 = Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text="2",command=lambda:btnClick(2)).grid(row=3,column=1)
btn3 = Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text="3",command=lambda:btnClick(3)).grid(row=3,column=2)
multiply = Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text="*",command=lambda:btnClick('*')).grid(row=3,column=3)
#forth row
btn0 = Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text="0",command=lambda:btnClick(0)).grid(row=4,column=0)
btnClear = Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text="C",command=btnClearDisplay).grid(row=4,column=1)
btnEquals = Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text="=",command=btnEqualInput).grid(row=4,column=2)
division = Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text="/",command=lambda:btnClick('/')).grid(row=4,column=3)

cal.mainloop()