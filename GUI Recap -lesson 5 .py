#Jessica Williams - Maths Quiz GUI Practice 11/2/21

'''Declare Parent class called MathsQuiz. All objects created from parent class'''
from tkinter import*

class MathsQuiz:
    #Use init method for all widgets
    def __init__(self, parent):

#Widgets for Welcome Frame
        
        self.Welcome = Frame(parent)
        self.Welcome.grid(row=0, column=0)

        self.TitleLable = Label(self.Welcome, text = "Welcome to Maths Quiz",
                                bg = "black", fg="white", width = 20, padx =30, pady = 10,
                                font = ("Time", '14', "bold italic"))
        self.TitleLable.grid(columnspan = 2)#Lable spans over two columns

        self.NextButton = Button(self.Welcome, text = 'Next')#ttk prefit gives modern Button
        self.NextButton.grid(row = 8, column = 1)

#Widgets for Questions Frame
        self.Questions = Frame(parent)
        self.Questions.grid(row=0, column=1)

        self.QuestionsLabel = Label(self.Questions, text = "Quiz Questions",
                                    bg= "black", fg="white", width= 20, padx = 30, pady = 10,
                                    font = ("Time", '14', "bold italic"))
        self.QuestionsLabel.grid(columnspan = 2)

        self.HomeButton = Button(self.Questions, text = 'Next')
        self.HomeButton.grid(row = 8, column = 1)


#Warning, Difficulty levvel label and Radio buttons
        self.WarningLabel = Label(self.Welcome, text = "", anchor= W,
                                  fg = "red", width = 20, padx = 30, pady = 10)
        self.WarningLabel.grid(row=4, columnspan = 2)

        self.DifficultyLabel = Label(self.Welcome, text = "Choose Difficulty level", anchor = W,
                                     fg = "black", width = 10, pady = 10, font = ("Time", '12', 'bold italic'))
        self.DifficultyLabel.grid(row =5, column = 0)

        self.difficulty = ["Easy", "Medium", "Hard"]
        self.diff_lvl = StringVar()
        self.diff_lvl.set(0)
        self.diff_btns = []

        for i in range(len(self.difficulty)):
            self.rb = Radiobutton(self.Welcome, variable = self.diff_lvl, value = i, text = self.difficulty[i],
                                  anchor = W, padx = 50, width = "5", height = "2")
            self.diff_btns.append(self.rb)
            self.rb.grid(row = i+6, column = 0, sticky = W)


        
#Main Routine
if __name__ == "__main__":#checks if condition - name of Parent class is main module
    root = Tk()
    frames = MathsQuiz(root)
    root.title("Quiz")
    root.mainloop() #binds the above commands together. 
