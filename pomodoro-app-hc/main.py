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
REPS = 0
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global REPS

    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    pomo_label.config(text="Timer", fg=GREEN)
    checkmark.config(text= "")
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        count_down(long_break_sec)
        pomo_label.config(text="Break", fg=RED)
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        pomo_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        pomo_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    global checkmark_text

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            marks += "✓"
            checkmark.config(text=f"{marks}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Productivity Application")
window.config(padx=100, pady=50, bg=YELLOW)

# create labels

# timer
pomo_label = Label(text="Timer", font=(FONT_NAME, 50))
pomo_label.grid(row=0, column=1)
pomo_label.config(fg=GREEN, bg=YELLOW)

# checkmark
checkmark = Label(font=(FONT_NAME, 40))
checkmark.grid(row=3, column=1)
checkmark.config(fg=GREEN, bg=YELLOW)

# buttons

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)
start_button.config(bg=YELLOW, highlightbackground=YELLOW)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)
reset_button.config(bg=YELLOW, highlightbackground=YELLOW)

# create canvas image for tomato
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file = "tomato.png") # way to read through a file to get image
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

window.mainloop()