from tkinter import *
import pyautogui
import time
import threading

# Create and initialize our main variables.

LENGTH = TIME = DELAY = CPS = SIDE = X = Y = 0.0
STOPED = True

# Create the main window.
window = Tk()

# Set the windows title.
window.title('Auto Clicker')

# Set the windows size.

window.geometry('462x133+78+78')

# Create functions.

def run():
    global LENGTH, TIME, DELAY, CPS, STOPED
    
    if STOPED:
        LENGTH = length_entry.get()
        DELAY = delay_entry.get()
        CPS = cps_entry.get()
        REPEAT = int(thread_entry.get())
        for i in range(REPEAT):
            threading.Thread(target=start).start()

def start():
    global STOPED, side
    time.sleep(int(DELAY))
    STOPED = False
    pyautogui.PAUSE = 0
    threading.Thread(target=wait).start()
    while True:
        if not STOPED:
            if side.get() == 'Right':
                if location.get() == 'current_location':
                    pyautogui.rightClick()
                else:
                    pyautogui.rightClick(x=float(x_location_entry.get()), y=float(y_location_entry.get()))
                time.sleep(1 / float(CPS))
            else:
                if location.get() == 'current_location':
                    pyautogui.leftClick()
                else:
                    pyautogui.leftClick(x=float(x_location_entry.get()), y=float(y_location_entry.get()))
                time.sleep(1 / float(CPS))
        else:
            break

def wait():
    global STOPED, LENGTH
    time.sleep(int(LENGTH))
    STOPED = True

def current_clicked():
    x_location_entry.config(state='disabled')
    y_location_entry.config(state='disabled')

def specific_clicked():
    x_location_entry.config(state='normal')
    y_location_entry.config(state='normal')

def handle_focus_in_x(_):
    x_location_entry.delete(0, END)
    x_location_entry.config(fg='black')

def handle_focus_out_x(_):
    x_location_entry.delete(0, END)
    x_location_entry.config(fg='grey')
    x_location_entry.insert(0, "x")

def handle_focus_in_y(_):
    y_location_entry.delete(0, END)
    y_location_entry.config(fg='black')

def handle_focus_out_y(_):
    y_location_entry.delete(0, END)
    y_location_entry.config(fg='grey')
    y_location_entry.insert(0, "y")
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
location.set("current_location")

location_label = Label(text='Cursor position')

current_location_button = Radiobutton(variable=location, value='current_location', text='Current Location', command=current_clicked)

specific_location_button = Radiobutton(variable=location, value='specific_location', text='Specific Location(x,y)', state="active", command=specific_clicked)
x_location_entry = Entry(width=4, state='disabled')
y_location_entry = Entry(width=4, state='disabled')

thread_label = Label(text='Threads')
thread_entry = Entry()

start_button = Button(text='Start', command=run)

# Add all the widgets to the window and position them.

length_label.grid(column=0, row=0, padx=25)
length_entry.grid(column=1, row=0)

delay_label.grid(column=0, row=1)
delay_entry.grid(column=1, row=1)

cps_label.grid(column=0, row=2)
cps_entry.grid(column=1, row=2)

thread_label.grid(column=0, row=3)
thread_entry.grid(column=1, row=3)

start_button.grid(column=0, row=4)

side_label.grid(column=3, row=0, padx=8)
side_option.grid(column=4, row=0)

location_label.grid(column=3, row=1)

current_location_button.grid(column=3, row=2, padx=8)

specific_location_button.grid(column=3, row=3)
x_location_entry.grid(column=4, row=3)
y_location_entry.grid(column=5, row=3)

# Run the main loop of the window.
window.mainloop()
