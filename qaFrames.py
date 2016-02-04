import Tkinter as tk
import tkMessageBox
import qGen as qg
import math 

class questionFrame:
    def __init__(self,parent,intro='Welcome'):
        self.master = parent
        frame = tk.Frame(parent)
        frame.pack(side='top')

        self.question = tk.StringVar()
        self.question.set(intro)

        self.hwtext = tk.Label(frame,textvariable=self.question,width=20,height=5)
        self.hwtext.pack(side='top')

class answerFrame:  
    def __init__(self,parent,numberOfAnswers):
        self.master = parent
        frame = tk.Frame(parent)
        frame.pack(side='top')

        self.ansSet = []
        for a in range(4):
            self.ansSet.append(tk.IntVar())
            self.ansSet[a].set(a)

        self.buttonSet = []
        for x in range(4):
            self.buttonSet.append(tk.Button(frame,textvariable=self.ansSet[x],command=lambda:response(self.ansSet[x].get())))
            frame.pack(side='top')
            
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
        
    ansSet[2].set(4)
    qm = qg.QuizMaster()
    qm.createQuestion()


    def response(answer):
        if not qm.checkAnswer(answer):
            tkMessageBox.Message(icon='info'
                    ,type='ok'
                    ,message=qm.answers['answer']).show()
            
            print qm.answers['answer']
        qm.createQuestion()
        decorativeString = "What is "+str(qm.q1)+"x"+str(qm.q2)+"?"    
        qFrame.question.set(decorativeString)
        answersList = qm.handoverAnswers()
        print answersList, qm.q1,qm.q2
        for a , b in zip(ansSet,answersList):
            a.set(b)
    
    width = int(math.sqrt(len(ansSet)))
    ButtonSet = []    
    for i,item in enumerate(ansSet):
        ButtonSet.append(tk.Button(answerFrame,textvariable=item,command=lambda item=item:response(item.get()),width=10,height=5))
        ButtonSet[i].grid(row=int(math.floor(i/width)),column=int(i%width))    


    def quit(event=None):
        root.destroy()

    root.bind('<q>',quit)

    root.mainloop()

