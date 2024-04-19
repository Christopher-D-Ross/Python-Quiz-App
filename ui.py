import tkinter
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    # Below is how you add the datatype of a parameter for a method.
    # quiz_brain: QuizBrain
    def __init__(self, quiz_brain: QuizBrain):
        # Adding self. to objects/variables turns them into properties which can be accessed anywhere in the class.
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzy")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text=f"Score: 0", foreground="white", bg=THEME_COLOR)
        self.score_label.grid(row=1, column=2)
        self.canvas = Canvas(height=250, width=300, bg="white", highlightthickness=0)
        # Adding pady to canvas.grid() added space between the canvas and score and buttons.
        self.canvas.grid(row=2, column=1, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Question To Be Asked By An Asker",
                                                     font=("Arial", 20, "italic"),
                                                     fill="black", width=260, justify=tkinter.CENTER)
        self.get_next_question()
        # self.score_label = Label(text=f"Score: 0", foreground="white", bg=THEME_COLOR)
        # self.score_label.grid(row=1, column=2)
        check_image = PhotoImage(file="images/true.png")
        self.check_button = Button(image=check_image, highlightthickness=0, borderwidth=0, command=self.check_if_answer_true)
        self.check_button.grid(row=3, column=1)
        x_image = PhotoImage(file="images/false.png")
        self.x_button = Button(image=x_image, highlightthickness=0, borderwidth=0, command=self.check_if_answer_false)
        self.x_button.grid(row=3, column=2)

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, fill="black", text=q_text)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, text="There are no more questions.")
            self.check_button.config(state="disabled")
            self.x_button.config(state="disabled")

    def check_if_answer_true(self):
        answer = self.quiz.check_answer("True")
        self.give_feedback(answer)

    def check_if_answer_false(self):
        answer = self.quiz.check_answer("False")
        self.give_feedback(answer)

    def give_feedback(self, correct):
        if correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        # time.sleep() can't be used in parallel with .mainloop()
        self.window.after(1000, self.get_next_question)
