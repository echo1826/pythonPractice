from tkinter import *

window = Tk()
window.minsize(width=300, height=100)
window.config(padx=30, pady=30)
window.title("Miles to Kilometers")

def click_handler():
    miles = miles_input.get()
    kilometers = float(miles) * 1.609344
    km.config(text=kilometers)


miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)


miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_question = Label(text="is equal to")
km_question.grid(column=0, row=1)

km = Label(text="0")
km.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calc_button = Button(text="Calculate", command=click_handler)
calc_button.grid(column=1, row=2)


window.mainloop()