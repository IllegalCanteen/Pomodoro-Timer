from tkinter import *
from math import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer=None
REP=1

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50,bg=YELLOW)

heading=Label(window,text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,40,"bold"))
heading.grid(column=1,row=0)



def start():
    global REP
    if REP % 2 != 0:
        heading.config(text="Work",fg=GREEN)
        count_down(WORK_MIN*60)
        REP += 1
    elif REP % 2 == 0 and REP % 8 != 0:
        heading.config(text="Break",fg=RED)
        count_down(SHORT_BREAK_MIN*60)
        REP += 1
    else:
        heading.config(text="Break",fg=PINK)
        count_down(LONG_BREAK_MIN*60)
        REP += 1
    start_button.config(state=DISABLED)




canvas=Canvas(window,width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato)
timer_text=canvas.create_text(100,130,text="00.00",fill="white",font=(FONT_NAME,40,"bold"))
canvas.grid(column=1,row=1)

def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    global REP
    REP = 1
    start_button.config(state="normal")
def count_down(count):
    global timer
    count_minutes = floor(count /60)
    count_seconds = count % 60
    if count_seconds ==0:
        count_seconds = "00"
    if 10 > int(count_seconds) > 0:
        count_seconds = "0"+str(count_seconds)
    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        timer=window.after(1000, count_down,count -1)
    else:
        start()
        if REP%2 != 0 and REP != 1:
            times_done.config(text="✔"*floor(REP/2))


start_button=Button(text="Start",command=start,highlightthickness=0)
start_button.grid(column=0,row=2)

reset_button=Button(text="Reset",command=reset,highlightthickness=0)
reset_button.grid(column=2,row=2)



times_done=Label(text="",font=(FONT_NAME,20,"normal"),bg=YELLOW)
times_done.grid(column=1,row=3)
window.mainloop()
