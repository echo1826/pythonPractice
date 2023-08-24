import tkinter

# initializes the window for the gui
window = tkinter.Tk()
window.title("GUI")
window.minsize(width=500, height=300)

# Label
label = tkinter.Label(text="I am a Label", font=("Arial", 24))
# .pack() will render the component to the screen
label.pack()
label["text"] = "New Text"
label.config(text="More New Text")



def click_handler():
    label.config(text=input.get())
# command is an event listener for on click
button = tkinter.Button(text="Click Me", command=click_handler)
button.pack()

# input
input = tkinter.Entry(width=10)
input.pack()


# keeps window on screen
window.mainloop()