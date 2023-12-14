from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class UserInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.label = Label(text=f"Score:{self.quiz.score}", font=("Arial", 10), bg=THEME_COLOR, foreground="white")
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280,
                                                     text="Question text", font=("Arial", 20, "italic"),
                                                     fill="black")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        img1 = PhotoImage(file="images/true.png")
        self.true_button = Button(image=img1, highlightthickness=0, bd=0, command=self.true_answer)
        self.true_button.grid(row=2, column=0, pady=20)

        img2 = PhotoImage(file="images/false.png")
        self.false_button = Button(image=img2, highlightthickness=0, bd=0, command=self.false_answer)
        self.false_button.grid(row=2, column=1, pady=20)

        self.get_question()

        self.window.mainloop()

    def get_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score:{self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_answer(self):
        self.changes(self.quiz.check_answer(True))

    def false_answer(self):
        self.changes(self.quiz.check_answer(False))

    def changes(self, feedback):
        if feedback:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_question)

