from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TIMER_FONT = ("Arial", 30, "")
BUTTON_FONT = ("Arial", 12, "")
CHECK_FONT = ("Arial", 15, "bold")
CHECK_MARK = "✔"
reps = 0
timer = None

# The reset button


def reset_timer():
    window.after_cancel(timer)
    label_timer.config(text="TIMER", fg=GREEN)
    canvas.itemconfig(timer_text, text=f"00:00")
    label_check.config(text="")
    global reps
    reps = 0


# The start button
# First calls the

def start_time():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If it is the 8th REP
    if reps % 8 == 0:
        count_down(long_break_sec)
        label_timer.config(text="BREAK", fg=RED)
    # If it is the 2nd/4th/6th REP
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label_timer.config(text="BREAK", fg=PINK)
    else:
        count_down(work_sec)
        label_timer.config(text="WORK", fg=GREEN)


# Means to countdown
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:                               # code below here restarts the required timer and displays checkmarks
        start_time()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += CHECK_MARK
        label_check.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

# Configure the window
window = Tk()
window.title("Pomodoro")
# window.minsize(width=500, height=300)
window.config(padx=100, pady=50, bg=YELLOW)

# Label that says timer is configured here
label_timer = Label(text="TIMER", font=TIMER_FONT, fg=GREEN, bg=YELLOW)
label_timer.grid(column=1, row=0)
label_timer.config(padx=0, pady=10)

# create canvas and insert image
# set the text creation to a variable for reconfiguration
canvas = Canvas(width=200, height=226, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# create button "start"
button_start = Button(text="Start", font=BUTTON_FONT, highlightthickness=0, command=start_time)
button_start.grid(column=0, row=2)

# create button reset
button_reset = Button(text="Reset", font=BUTTON_FONT, highlightthickness=0, command=reset_timer)
button_reset.grid(column=2, row=2)

# place checkmark
label_check = Label(fg=GREEN, bg=YELLOW, font=CHECK_FONT)
label_check.grid(column=1, row=3)


window.mainloop()
