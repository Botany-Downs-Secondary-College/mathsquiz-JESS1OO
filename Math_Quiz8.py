from tkinter import *
from tkinter import ttk


class MathQuiz:
    def __init__(self, parent):
        self.Welcome = Frame(parent)
        self.Welcome.grid(row=0, column=0)

        self.TitleLabel = Label(self.Welcome, text="Welcome to Maths Quiz",
                                bg="black", fg="white", width=20, padx=30, pady=10,
                                font=("Time", '14', "bold italic"))
        self.TitleLabel.grid(columnspan=2)

        self.NextButton = ttk.Button(self.Welcome, text="Next", command=self.show_questions)
        self.NextButton.grid(row=9, column=0, columnspan=2, pady=10)

        self.Questions = Frame(parent)
        self.Questions.grid(row=0, column=1)

        self.QuestionsLabel = Label(self.Questions, text="Quiz Questions", bg = "black", fg ="white",
                                    width=20, padx=30, pady=10, font=("Time", "14", "bold italic"))
        self.QuestionsLabel.grid(columnspan=2)

        self.HomeButton = ttk.Button(self.Questions, text="Home", command=self.show_welcome)
        self.HomeButton.grid(row=8, column=1, columnspan=2)

        self.NameLabel = Label(self.Welcome, text="Name", anchor=W, fg="black", width=17, pady=10,
                               font=("Time", "12", "bold italic"))
        self.NameLabel.grid(row=1, column=1, columnspan=5)

        self.NameEntry = ttk.Entry(self.Welcome, width=20)
        self.NameEntry.grid(row=2, column=0, columnspan=2)

        self.AgeLabel = Label(self.Welcome, text="Age", anchor=W, width=16, fg="black", pady=10,
                              font=("Time", "12", "bold italic"))
        self.AgeLabel.grid(row=3, column=1, columnspan=2)

        self.AgeEntry = ttk.Entry(self.Welcome, width=20)
        self.AgeEntry.grid(row=4, column=0, columnspan=2)

        self.DifficultyLabel = Label(self.Welcome, text="Choose Difficulty level", anchor=W,
                                     fg="black", width=20, pady=10, font=("Time", '12', 'bold italic'))
        self.DifficultyLabel.grid(row=5, column=0, columnspan=2)

        self.difficulty = ["Easy", "Medium", "Hard"]
        self.diff_lvl = StringVar()
        self.diff_lvl.set(0)
        self.diff_btns = []

        for i in range(len(self.difficulty)):
            self.rb = Radiobutton(self.Welcome, variable=self.diff_lvl, value=i, text=self.difficulty[i],
                                  anchor=W, padx=50, width="5", height="1")
            self.diff_btns.append(self.rb)
            self.rb.grid(row=i + 6, column=0, columnspan=2)

    def show_welcome(self):
        self.Questions.grid_remove()
        self.Welcome.grid()

    def show_questions(self):
        self.Welcome.grid_remove()
        self.Questions.grid()


"""Main routine"""
if __name__ == "__main__":
    root = Tk()
    frames = MathQuiz(root)
    root.title("Quiz")
    root.mainloop()
