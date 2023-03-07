#!/bin/bash 
from serial import Serial # pySerial = USB Serial port library
from tkinter import *   # Tkinter = GUI library, importing the entire library with *

import serial.tools.list_ports
import pyvisa
import matplotlib.pyplot as plt

import time # Time module to keep track of time

from matplotlib.lines import Line2D


#####################################################################################################################################################

## Functions for the programme

# Define our switch function

def switch():

    global is_on
    
    # Determine is on or off
    if is_on==False:
        on_button.config(image = on)
        # The Switch is switched On
        is_on = True
        ser.write(b"OUT1\n")


    else:
        on_button.config(image = off)
        # The Switch is switched Off
        is_on = False
        ser.write(b"OUT0\n")

def setting_1():

    global time_1, time_2

    ser.write(bytes("VSET1:4\n", encoding = "ascii"))  
    ser.write(bytes("ISET1:0.3\n", encoding = "ascii"))
 

def setting_2():

    global time_1, time_2

    ser.write(bytes("VSET1:6\n", encoding = "ascii"))
    ser.write(bytes("ISET1:0.5\n", encoding = "ascii"))



def auto():

    global time_1, time_2

    global start

    new_3a = Toplevel()
    new_3a.title("Operations_3a")  
    new_3a.iconbitmap("Cord.ico")
    new_3a.geometry("300x300")

    l_3a = Label(new_3a, text = 'OPERATION IN PROGRESS').pack(ipadx = 30, ipady= 30)

    new_3a.after(int(time_1.get()), setting_1)
    
    new_3a.after(int(time_2.get()), setting_2)

    


# Identifying the device

def opt_1():   
    
    new_1 = Toplevel()
    new_1.title("Operations_1")  
    new_1.iconbitmap("Cord.ico")
    new_1.geometry("400x300")
    
    l1= Label(new_1, text= "Test command" + "*IDN?")
    l1.grid(row= 2, column = 2, padx= 20, pady = 20)

    ser.write(b"*IDN?\r") # Carriage return to be included as a terminator for query commands

    # Include the b prefix before the command to convert it into bytes for easier communication between the laptop and the power supply

    l1a= Label(new_1, bd= 2, text= "Response: " + ser.readline().decode())
    l1a.grid(row= 5, column = 2, padx= 20, pady = 20)

# One Time commands function description 

def opt_2():  

    new_2 = Toplevel()
    new_2.title("Operations_2")
    new_2.iconbitmap("Cord.ico")  
    new_2.geometry("500x500")

    global on, off,on_button, is_on

    """
    out_2= [
            ('ON',1),
            ('OFF',0)
            ]
    choice = StringVar()
    choice.set('OFF')
    
    for cond,val in out_2:
        Radiobutton(new, text= cond, padx = 20, pady = 20, variable= choice, value = val).pack(anchor='w')

    """ 
 
    # Define Our Images for the ON/OFF switch
    on = PhotoImage(file = "on.png")
    off = PhotoImage(file = "off.png")
 
    # Create A Button for the ON/OFF switch
    if is_on==False:
        on_button = Button(new_2, image = off, bd = 2, command = switch)
        on_button.pack(padx= 10, pady = 10)

    else:
        on_button = Button(new_2, image = on, bd = 2, command = switch)
        on_button.pack(padx= 10, pady = 10)

    out_2= [
            ('Query','Query'),
            ('Command','Command')
            ]
    choice = StringVar()
    choice.set('Query')
    
    for cond,val in out_2:
        Radiobutton(new_2, text= cond, padx = 20, pady = 20, variable= choice, value = val).pack(anchor='s')

    def one_open():

        new_2a= Toplevel()
        new_2a.title("Operations_2a")
        new_2a.iconbitmap("Cord.ico")  
        new_2a.geometry("300x300")


        e = Entry(new_2a, width= 50)
        e.pack(ipady= 10)

        def defin():

            if choice.get()=='Query':
                ser.write(bytes(str(e.get()), encoding= "ascii") + b'\r' )
                l2= Label(new_2a, bd= 2, text= "Response: " + ser.readline().decode())
                l2.pack(padx= 10, pady = 10)

            else:
                #l2= Label(new_2a, text= "Command executed: " + " " + e.get()).pack(padx= 20, pady=20)
                ser.write(bytes(str(e.get()), encoding= "ascii") + b'\n' )

            #new_2a.after(5000, l2.destroy())

        b_2a= Button(new_2a,text= "Submit", command= defin)
        b_2a.pack(padx= 10, pady= 10)
        
    b2= Button(new_2,text= "Submit", command= one_open)
    b2.pack(padx= 10, pady= 10)
 
# Automated change - THERMAL BALANCE TEST

def opt_3():
    
    new_3 = Toplevel()
    new_3.title("Operations_3")  
    new_3.iconbitmap("Cord.ico")  
    new_3.geometry("500x500")
    
    global  on_button, time_1, time_2, on, off

    
    on = PhotoImage(file = "on.png")
    off = PhotoImage(file = "off.png")

    # Create A Button for the ON/OFF switch
    if is_on==False:
        on_button = Button(new_3, image = off, bd = 2, command = switch)
        on_button.pack(padx= 10, pady = 10)

    else:
        on_button = Button(new_3, image = on, bd = 2, command = switch)
        on_button.pack(padx= 10, pady = 10)


    # Entry fields for the timesteps

    l_3a= Label(new_3, bd= 2, text= 'Enter the first time step (milliseconds)')
    l_3a.pack(padx= 10, pady = 10)

    time_1 = Entry(new_3, width= 50)        # Time step 1
    time_1.pack(padx= 10, pady = 10)

    l_3b= Label(new_3, bd= 2, text= 'Enter the second time step (milliseconds)' )
    l_3b.pack(padx= 10, pady = 10)

    time_2 = Entry(new_3, width= 50)        # Time step 2
    time_2.pack(padx= 10, pady = 10)

    b3= Button(new_3,text= "Submit", command= auto)
    b3.pack(padx= 10, pady= 10)

    
    
def opt_4():

    ser.write(b'OUT0\n')

    l4 = Label(main_menu, text= 'The programme will end in 5 seconds')
    l4.grid(row= 4, column = 1, padx= 10, pady= 10)

    main_menu.after(5000, main_menu.destroy)

    #b4= Button(main_menu,text= "END Program", command= main_menu.quit)
    #b4.grid(row=6, column= 1, padx= 10, pady= 10)
  

def open():
        
    if(o1.get() == options[0]):
        opt_1()
        
            
    elif(o1.get() == options[1]):
        opt_2()
        
            
    elif(o1.get() == options[2]):
        opt_3()
          
        
    elif(o1.get() == options[3]):
        opt_4()

def open_1():

    # Setup the plot

    plt.figure(figsize=(7,7)) # Initialize a matplotlib figure
    plt.xlabel('Elapsed Time (s)', fontsize=24) # Create a label for the x axis and set the font size to 24pt
    plt.xticks(fontsize=18) # Set the font size of the x tick numbers to 18pt
    plt.ylabel('Measurement', fontsize=24) # Create a label for the y axis and set the font size to 24pt
    plt.yticks(fontsize=18) # Set the font size of the y tick numbers to 18pt

    plt.title("Voltage and current measurements for channel 1") # Gives a title to the plot 

    
    
    # Create a while loop that continuously measures and plots data from the GPD 4303S until the programme quits
    while True:

        # ser.write(b'VOUT1?\r')
        # voltageReading = float(ser.readline().decode().split('\r')[0][:-2]) # Read and process data from the power supply. 
        # voltageList.append(voltageReading) # Append processed data to the voltage list

        ser.write(b'IOUT1?\r')
        currentReading = float(ser.readline().decode().split('\r')[0][:-2]) # Read and process data from the power supply. 
        currentList.append(currentReading) # Append processed data to the current list

        timeList.append(float(time.time() - startTime)) # Append time values to the time list
        time.sleep(0.5) # Interval to wait between collecting data points.


        #plt.plot(timeList, voltageList, color='blue', linewidth=2.5) # Plot the collected data with time on the x axis and temperature on the y axis.
        plt.plot(timeList, currentList, color='green', linewidth=2.5)

        #plt.legend(["Voltage","Current"], loc='upper right')
        plt.tight_layout()
        
        plt.pause(0.01) # This command is required for live plotting. This allows the code to keep running while the plot is shown.

    

      

################################################################################################################################################

## Main programme 

if __name__ == "__main__":

    global is_on

    timeList = [] # Create an empty list to store time values in.
    voltageList = [] # Create an empty list to store voltage values in.
    currentList = [] # Create an empty list to store current values in.
    startTime = time.time() # Create a variable that holds the starting timestamp.


    print("Detected serial ports: ")

    for p in serial.tools.list_ports.comports():
        print("  " + p.device + " - " + p.description)
    
    print()

    port = input("Type in port name for GPD 4303s: ")
    
    print()

    ser= Serial(port, baudrate=9600) 

    ser.write(b'STATUS?\r')

    set_v = ser.readline().decode()

    mode= set_v[5]

    print("Status bit - " + set_v)

    print("Output mode (ON 1/OFF 0)" + mode)

    mode = int(set_v[5])

    if mode==0:
        is_on = False

    else:
        is_on = True

    main_menu= Tk() # Tkinter widget creation command

    main_menu.title("Main Menu")
    main_menu.iconbitmap("Cord.ico")
    main_menu.geometry("400x400")

    options = [
    
        'Test sequence (*IDN?)',
        'One-Time commands',
        'Automated voltage and current setting',
        'QUIT PROGRAM' 
        ]

    # Variable that holds the value of the options, passed onto the Option menu mentioned below
    o1= StringVar()  
    o1.set(options[0])

    # Creates the Drop-down menu in the main widget
    drop = OptionMenu(main_menu, o1, *options ) 
    drop.grid(row=1, column= 1, padx= 10, pady= 10)

    # Creates the submit button for the main widget
    b_main= Button(main_menu,text= "Submit", command= open)
    b_main.grid(row=1, column= 2, padx= 10, pady= 10)

    # Creates the graph button for the main widget
    b1_main= Button(main_menu,text= "Graph", command= open_1)
    b1_main.grid(row=8, column= 2, padx= 20, pady= 20)

    mainloop()
