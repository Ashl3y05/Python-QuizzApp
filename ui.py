from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("The Best Quiz App in the World")
        self.window.config(padx=20,pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score:",bg=THEME_COLOR, highlightthickness=0,fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150, 125,
            width=280,
            fill=THEME_COLOR,
            text=f"Sample Question",
            font=("Ariel", 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2,pady=50)

        self.true_file = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=self.true_file,)
        self.true_button.grid(column=0,row=2)

        self.false_file = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=self.false_file, )
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        question_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=question_text)
