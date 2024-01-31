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
        self.quiz_text = self.canvas.create_text(150, 125, font=("Arial", 20, "italic"), text="Quiz App", width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_button_press)
        self.true_button.grid(row=3, column=0)
        
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_button_press)
        self.false_button.grid(row=3, column=1)
        
        self.show_next_question()
        
        self.window.mainloop()
        
    def show_next_question(self):
        self.canvas.configure(bg="#ffffff")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            next_question = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_text, text=next_question)
        else:
            self.canvas.itemconfig(self.quiz_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        
    def true_button_press(self):
        result = self.quiz.check_answer("True")
        self.give_feedback(result)
        
    def false_button_press(self):
        result = self.quiz.check_answer("False")
        self.give_feedback(result)
        
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.show_next_question)