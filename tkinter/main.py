import tkinter

# initializes the window for the gui
window = tkinter.Tk()
window.title("GUI")
window.minsize(width=500, height=300)

# Label
label = tkinter.Label(text="I am a Label", font=("Arial", 24))
# .pack() will render the component to the screen
label.pack()

# keeps window on screen
window.mainloop()