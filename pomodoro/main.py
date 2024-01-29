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
reps = 0
checkmark = ""
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60
    if reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        countdown(short_break_seconds)
    elif reps % 8 == 0:
        timer_label.config(text="Break", fg=PINK)
        countdown(long_break_seconds)
    else:
        timer_label.config(text="Work", fg=GREEN)
        countdown(work_seconds)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(counter):
    minutes = math.floor(counter / 60)
    seconds = counter % 60
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if counter > 0:
        window.after(1000, countdown, counter - 1)
    else:
        global reps
        if reps % 2 == 0:
            checkmark += "✔"
            checkmark_label.config(text=checkmark)
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)


timer_label = Label(text="Timer", font=("Arial", 24, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1)


canvas = Canvas(width=200, height=224, bg=YELLOW)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_image)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=("Arial", 30, "bold"))
canvas.grid(row=1, column=1)


start_btn = Button(text="Start", command=start_timer)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset")
reset_btn.grid(row=2, column=3)


checkmark_label = Label(bg=YELLOW, fg=GREEN)
checkmark_label.grid(row=3, column=1)


window.mainloop()