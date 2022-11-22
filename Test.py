#!/bin/bash 
from serial import Serial # pySerial = USB Serial port library
from tkinter import *   # Tkinter = GUI library

main_menu= Tk()

import serial.tools.list_ports

import time # Time module to keep track of time

main_menu.title("Main Menu")
main_menu.iconbitmap("Cord.ico")
main_menu.geometry("400x400")


def opt_1():
    
    
    new = Toplevel()
    new.title("Operations")  
    new.geometry("200x200")
    
    l1= Label(new, text= "Test command" "*IDN?")
    l1.grid(row= 2, column = 2, padx= 20, pady = 20)
    

def opt_2():
    
    
    new = Toplevel()
    new.title("Operations")  
    new.geometry("200x200")
    
    out_2= [
            ('ON',1),
            ('OFF',0)
            ]
    choice = StringVar()
    choice.set('OFF')
    
    for cond,val in out_2:
        Radiobutton(new, text= cond, padx = 20, pady = 20, variable= choice, value = val).pack(anchor='w')
        
    
    l2= Label(new, text = choice)
    l2.pack(anchor='s')  


def opt_3():
    
    
    new = Toplevel()
    new.title("Operations")  
    new.geometry("200x200")
    
    e = Entry(new, width= 50)
    e.pack()
    
    
    # time.sleep(2.5)
    # e.delete(0,END)
    
def opt_4():
    
    
    new = Toplevel()
    new.title("Operations")  
    new.geometry("200x200")

    l4= Label(new, text="In progress")
    l4.grid(row= 2, column = 2, padx= 20, pady = 20)
    

def open():
        
    if(o1.get() == options[0]):
        opt_1()
        
            
    elif(o1.get() == options[1]):
        opt_2()
        
            
    elif(o1.get() == options[2]):
        opt_3()
          
        
    elif(o1.get() == options[3]):
        opt_4()
        
    
        

options = [
    
        'Test sequence (*IDN?)',
        'Output Switch (ON/OFF)',
        'One-Time commands',
        'Automated voltage and current setting' 
        ]

o1= StringVar() # Variable that holds the value of the options, passed onto the 
o1.set(options[0])

drop = OptionMenu(main_menu, o1, *options ) # Creates the Drop-down menu
drop.grid(row=1, column= 1, padx= 10, pady= 10)


b1= Button(main_menu,text= "Submit", command= open)
b1.grid(row=1, column= 2, padx= 10, pady= 10)

#new.mainloop()

#main_menu.mainloop()

mainloop()





