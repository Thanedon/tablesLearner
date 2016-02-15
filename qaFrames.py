import Tkinter as tk
import tkMessageBox
import math
import random as rd 
#only needed for main
import qGen as qg

class QuestionFrame(tk.Frame):
    def __init__(self,parent):
        tk.Frame.__init__(self,parent)

        self.question = tk.StringVar()
        self.question.set('Welcome')

        self.hwtext = tk.Label(self,textvariable=self.question,width=20,height=5)
        self.hwtext.pack(side='top')

    def updateQuestion(self,multiples):
        print multiples
        self.buffer = "What is "+str(multiples[0])+"x"+str(multiples[1])+"?"
        self.question.set(self.buffer)

class MultiChoiceAnswerFrame(tk.Frame):  
    def __init__(self,parent,quizMaster,magicnumber=4):
        tk.Frame.__init__(self,parent)
        self.qm = quizMaster
        self.noOfChoices = magicnumber
        
        self.ansSet = []
        for a in range(self.noOfChoices):
            self.ansSet.append(tk.IntVar())
            self.ansSet[a].set(a)

        self.width = int(math.sqrt(self.noOfChoices))
        self.buttonSet = []
        for i,item in enumerate(self.ansSet):
            self.buttonSet.append(tk.Button(self,textvariable=item,command=lambda item=item:quizMaster.receiveAnswer(item.get(),self)))
            self.buttonSet[i].grid(row=int(math.floor(i/self.width)),column=int(i%self.width))    
        
    def updateAnsSet(self,newAnswers):
        for a,b in zip(self.ansSet,newAnswers):
            a.set(b)

    def refresh(self):
        answers = qg.answerGen(self.qm.q1,self.qm.q2,self.noOfChoices-1)
        answers.append(self.qm.answer)
        rd.shuffle(answers)
        self.updateAnsSet(answers)

class TypedResponseAnswerFrame(tk.Frame):
    def __init__(self,parent,quizmaster):
        tk.Frame.__init__(self,parent)

        self.ans = tk.StringVar()
        ansEntry = tk.Entry(self,textvariable=self.ans)
        ansEntry.pack(side='top')
        ansEntry.bind('<KP_Enter>',self.returnAnswer)
    
        self.qm = quizmaster

    def printTextdd(self,event=None):
        print self.ans.get()

    def returnAnswer(self,event=None):
        try:
            self.qm.receiveAnswer(int(self.ans.get()),self)
        except ValueError:
            print 'hey Nnamdi'

    def refresh(self):
        self.ans.set('')

def main():            
    #generate root
    root = tk.Tk()
    #attach mainFrame
    mainFrame = tk.Frame(root)
    mainFrame.pack(side='top')
    #create questionFrame
    qFrame = QuestionFrame(mainFrame)
    qFrame.pack(side='top')
    #create Quizmaster to handle question generation and answer checking
    aFrame = MultiChoiceAnswerFrame(mainFrame,qm)
    #aFrame = TypedResponseAnswerFrame(mainFrame)
    aFrame.pack(side='top')    

    def quit(event=None):
        root.destroy()

    root.bind('<q>',quit)
    
    root.mainloop()

if __name__ == '__main__':
    main()

