#Jessica Williams - Maths Quiz GUI Practice 11/2/21

'''Declare Parent class called MathsQuiz. All objects created from parent class'''
from tkinter import*

class MathsQuiz:
    #Use init method for all widgets
    def __init__(self, parent):

#Widgets for Welcome Frame
        
        self.welcome = Frame(parent)
        self.welcome.grid(row=0, column=0)

        self.TitleLable = Label(self.welcome, text = "Welcome to Maths Quiz",
                                bg = "black", fg="white", width = 20, padx =30, pady = 10,
                                font = ("Time", '14', "bold italic"))
        self.TitleLable.grid(columnspan = 2)

        self.NextButton = Button(self.welcome, text = 'Next')
        self.NextButton.grid(row = 8, column = 1)

#Main Routine
if __name__ == "__main__":
    root = Tk()
    frames = MathsQuiz(root)
    root.title("Quiz")
    root.mainloop()
