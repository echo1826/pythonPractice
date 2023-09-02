from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=("Arial", 24, "bold"), bg=YELLOW, fg=GREEN)
timer_label.pack()


canvas = Canvas(width=200, height=224, bg=YELLOW)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_image)
canvas.create_text(103, 130, text="00:00", fill="white", font=("Arial", 30, "bold"))
canvas.pack()


start_btn = Button(text="Start")
start_btn.pack(side="right")

reset_btn = Button(text="Reset")
reset_btn.pack(side="left")

window.mainloop()