from tkinter import *
import pyautogui
import time
import threading

# Create and initialize our main variables.

LENGTH = TIME = DELAY = CPS = SIDE = X = Y = 0.0
STOP = True

# Create the main window.
window = Tk()

# Set the windows title.
window.title('Auto Clicker')

# Set the windows size.

window.geometry('425x110+78+78')

# Create functions.

def run():
    print(window.geometry())
    global LENGTH, TIME, DELAY, CPS, STOP
    
    if STOP:
        LENGTH = length_entry.get()
        DELAY = delay_entry.get()
        CPS = cps_entry.get()
        threading.Thread(target=start).start()

def start():
    global STOP, side
    time.sleep(int(DELAY))
    STOP = False
    pyautogui.PAUSE = 0
    threading.Thread(target=wait).start()
    while True:
        if not STOP:
            if side.get() == 'Right':
                pyautogui.rightClick()
                time.sleep(1 / float(CPS))
            else:
                pyautogui.leftClick()
                time.sleep(1 / float(CPS))
        else:
            break

def wait():
    global STOP, LENGTH
    time.sleep(int(LENGTH))
    STOP = True

# Create the widgets.

length_label = Label(text='Length')
length_entry = Entry()

delay_label = Label(text='Delay')
delay_entry = Entry()

cps_label = Label(text='CPS')
cps_entry = Entry()

side = StringVar(value='Left')
side_label = Label(text='Mouse Button')
side_option = OptionMenu(window, side, "Left", "Right")

location = StringVar()
location_label = Label(text='Cursor position')
current_location_button = Radiobutton(variable=location, value='current_location', text='Current Location')

start_button = Button(text='Start', command=run)

# Add all the widgets to the window and position them.

length_label.grid(column=0, row=0, padx=25)
length_entry.grid(column=1, row=0)

delay_label.grid(column=0, row=1)
delay_entry.grid(column=1, row=1)

cps_label.grid(column=0, row=2)
cps_entry.grid(column=1, row=2)

start_button.grid(column=0, row=3)

side_label.grid(column=3, row=0, padx=8)
side_option.grid(column=4, row=0)

location_label.grid(column=3, row=1)
current_location_button.grid(column=3, row=2, padx=8)

# Run the main loop of the window.
window.mainloop()