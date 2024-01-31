from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain): #quiz_brain: QuizBrain is declaring the type of what the parameter quiz_brain is going to come in as
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="#ffffff", font=("Arial", 15))
        self.score_label.grid(row=0, column=1)
        
        self.canvas = Canvas(width=300, height=250)
        self.quiz_text = self.canvas.create_text(150, 125, font=("Arial", 20, "italic"), text="Quiz App")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0)
        self.true_button.grid(row=3, column=0)
        
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0)
        self.false_button.grid(row=3, column=1)
        
        self.window.mainloop()
        
    def show_next_question(self):
        next_question = self.quiz.next_question()