#Jessica Williams - Maths Quiz GUI Practice 11/2/21

'''Declare Parent class called MathsQuiz. All objects created from parent class'''
from tkinter import*
from tkinter import ttk
from random import*


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

        self.next_button = Button(self.Welcome, text = 'Next')#ttk prefit gives modern Button
        self.next_button.grid(row = 8, column = 1)

#Widgets for Questions Frame
        self.Questions = Frame(parent)
        self.Questions.grid(row=0, column=1)

        self.QuestionsLabel = Label(self.Questions, text = "Quiz Questions",
                                    bg= "black", fg="white", width= 20, padx = 30, pady = 10,
                                    font = ("Time", '14', "bold italic"))
        self.QuestionsLabel.grid(columnspan = 2)

        self.HomeButton = Button(self.Questions, text = 'Home', command = self.show_Welcome)
        self.HomeButton.grid(row = 8, column = 1)

        self.Problems = Label(self.Questions, text= "")
        self.Problems.grid(row = 1, column = 0)
        
        self.next_button(self.Questions, text = "Next Question", command = self.next_question)
        self.next_button.grid(row= 8, column =1)
    

#Warning, Difficulty levvel label and Radio buttons
        self.WarningLabel = Label(self.Welcome, text = "", anchor= W,
                                  fg = "red", width = 20, padx = 30, pady = 10)
        self.WarningLabel.grid(row=4, columnspan = 2)

        self.DifficultyLabel = Label(self.Welcome, text = "Choose Difficulty level", anchor = W,
                                     fg = "black", width = 10, pady = 10, font = ("Time", '12', 'bold italic'))
        self.DifficultyLabel.grid(row =4, column = 0)

        self.difficulty = ["Easy", "Medium", "Hard"]
        self.diff_lvl = StringVar()
        self.diff_lvl.set(0)
        self.diff_btns = []

        for i in range(len(self.difficulty)):
            self.rb = Radiobutton(self.Welcome, variable = self.diff_lvl, value = i, text = self.difficulty[i],
                                  anchor = W, padx = 50, width = "5", height = "2")
            self.diff_btns.append(self.rb)
            self.rb.grid(row = i+6, column = 0, sticky = W)

            
        #Name and AGe Labels
        self.NameLabel = Label(self.Welcome, text = "Name", anchor = W, fg = "black", width =10, padx = 30, pady =10, font = ("Time",'12', "bold italic"))
        self.NameLabel.grid(row =2, column = 0)

        self.AgeLabel = Label(self.Welcome, text = "Age", anchor = W, fg = "black",padx = 30, pady = 10, font =("Time",'12', "bold italic"))
        self.AgeLabel.grid(row= 3, column = 0)
        #Name and age Entry

        self.NameEntry = ttk.Entry(self.Welcome, width = 20)
        self.NameEntry.grid(row = 2, column=1, columnspan =2)

        self.AgeEntry = ttk.Entry(self.Welcome, width = 20)
        self.AgeEntry.grid(row = 3, column = 1)


    def next_question(self):
        #Creates questions and stores answer
        x = randrage(10)
        y = randrange(10)
        self.answer = x + y

        questions_text = str(x) + "+" + str(y) + "="
        self.Problems.configure(text = question_text)

        
        

    # a method that removes questions frame
    def show_Welcome(self):
        self.Questions.grid_remove()
        self.Welcome.grid()
        
    def show_Questions(self):
        self.Welcome.grid_remove()
        self.Questions.grid()

    def show_Questions(self):
        try:

            if self.NameEntry.get() =="":
                self.WarningLabel.configure(text = "Please Enter Name")
                self.NameEntry.focus()

            elif self.NameEntry.get().isalpha() ==False:
                self.WarningLabel.configure(text = "PLease enter text")
                self.NameEntry.delete(0, END)
                self.NameEntry.focus()
            elif self.AgeEntry.get() =="":
                self.WarningLabel.configure(text = "PLease Enter age")
                self.AgeEntry.focus()

            elif int(self.AgeEntry.get()) > 12:
                self.WarningLabel.configure(text = "You are too old!")
                self.AgeEntry.delete(0, END)
                self.AgeEntry.focus()

            elif int(self.AgeEntry.get()) < 0:
                self.WarningLabel.configure(text = "You are too old!")
                self.AgeEntry.delete(0, END)
                self.AgeEntry.focus()

            elif int(self.AgeEntry.get()) < 7:
                self.WarningLabel.configure(text = "You are too young")
                self.AgeEntry.delete(0, END)
                self.AgeEntry.focus()

            else:
                self.Welcome.grid_remove()
                self.Questions.grid()
                
        except ValueError:
            self.WarningLabel.configure(text = "Please enter a number")
            self.AgeEntry.delete(0, END)
            self.AgeEntry.focus()


                
        
#Main Routine
if __name__ == "__main__":#checks if condition - name of Parent class is main module
    root = Tk()
    frames = MathsQuiz(root)
    root.title("Quiz")
    root.mainloop() #binds the above commands together. 
