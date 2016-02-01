import Tkinter as tk
import tkMessageBox
import qGen as qg

class questionFrame:
    def __init__(self,parent,intro='Welcome'):
        self.master = parent
        frame = tk.Frame(parent)
        frame.pack(side='top')

        self.question = tk.StringVar()
        self.question.set(intro)

        self.hwtext = tk.Label(frame,textvariable=self.question,width=20,height=10)
        self.hwtext.pack(side='top')

class answerFrame:  
    def __init__(self,parent,numberOfAnswers):
        self.master = parent
        frame = tk.Frame(parent)
        frame.pack(side='top')

        self.ansSet = []
        for a in range(4):
            ansSet.append(tk.IntVar())

        self.buttonSet = []
        for x in range(4):
            buttonSet.append(tk.Button(frame,textvariable=self.ansSet[x],command=lambda:multiply(self.ansSet[x].get())))
            
if __name__ == '__main__':
    #generate root
    root = tk.Tk()
    #attach mainFrame
    mainFrame = tk.Frame(root)
    mainFrame.pack(side='top')
    #create questionFrame
    qFrame = questionFrame(mainFrame)

    #create answerFrame
    answerFrame = tk.Frame(mainFrame)
    answerFrame.pack(side='top')
    
    ansSet = []
    for a in range(4):
        ansSet.append(tk.IntVar())
        
    qm = qg.QuizMaster()
    qm.createQuestion()


    def multiply(answer):
        if not qm.checkAnswer(answer):
            tkMessageBox.Message(icon='info'
                    ,type='ok'
                    ,message=qm.answers['answer']).show()
            
            print qm.answers['answer']
        qm.createQuestion()
        decorativeString = "What is "+str(qm.q1)+"x"+str(qm.q2)+"?"    
        print decorativeString
        qFrame.question.set(decorativeString)
        answersList = qm.answers['dummy'][:]
        answersList.append(qm.answers['answer'])
        print answersList, qm.q1,qm.q2
        for a , b in zip(ansSet,answersList):
            a.set(b)
    

    firstButton = tk.Button(answerFrame,textvariable=ansSet[0],command=lambda:multiply(ansSet[0].get()),width=10,height=10)
    firstButton.grid(row=0,column=0)    

    secondButton = tk.Button(answerFrame,textvariable=ansSet[1],command=lambda:multiply(ansSet[1].get()),width=10,height=10)
    secondButton.grid(row=0,column=1)    
    
    thirdButton = tk.Button(answerFrame,textvariable=ansSet[2],command=lambda:multiply(ansSet[2].get()),width=10,height=10)
    thirdButton.grid(row=1,column=0)    

    fourthButton = tk.Button(answerFrame,textvariable=ansSet[3],command=lambda:multiply(ansSet[3].get()),width=10,height=10)
    fourthButton.grid(row=1,column=1)    

    def quit(event=None):
        root.destroy()

    root.bind('<q>',quit)

    root.mainloop()

