from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("The Best Quiz App in the World")
        self.window.config(padx=20,pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0",bg=THEME_COLOR, highlightthickness=0,fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125,
            width=280,
            fill=THEME_COLOR,
            text=f"Sample Question",
            font=("Ariel", 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2,pady=50)

        true_file = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_file, command=self.true_pressed)
        self.true_button.grid(column=0,row=2)

        false_file = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_file, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of the quiz.\n "
                                                            f"Your score: {self.quiz.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
