import tkinter

# initializes the window for the gui
window = tkinter.Tk()
window.title("GUI")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

def click_handler():
    label.config(text=input.get())

# Label
label = tkinter.Label(text="I am a Label", font=("Arial", 24))
# .pack() will render the component to the screen
# label.pack()

# .place() is a more precise rendering method that uses x-y coodinates
# x=0, y=0 will place the component at the top left corner of the window
# label.place(x=100, y=200)

# .grid() uses columns and rows to render the component
# grid is relative to other components, meaning you should start with the component you want to appear first then use grid to render the next components to place them in other rows or columns
label.grid(column=0, row=0)
label["text"] = "New Text"
label.config(padx=20, pady=20)

challenge_button = tkinter.Button(text="New Button")
challenge_button.grid(column=3, row=0)

# command is an event listener for on click
button = tkinter.Button(text="Click Me", command=click_handler)
# button.pack()
button.grid(column=2, row=1)

# input
input = tkinter.Entry(width=10)
# input.pack()
input.grid(column=4, row=3)

# keeps window on screen
window.mainloop()
