import Tkinter as tk
import tkMessageBox
import qGen as qg
import math 

class questionFrame(tk.Frame):
    def __init__(self,parent,intro='Welcome'):
        tk.Frame.__init__(self,parent)

        self.question = tk.StringVar()
        self.question.set(intro)

        self.hwtext = tk.Label(self,textvariable=self.question,width=20,height=5)
        self.hwtext.pack(side='top')

    def updateQuestion(self,first,second):
        self.buffer = "What is "+str(first)+"x"+str(second)+"?"
        self.question.set(self.buffer)


class answerFrame(tk.Frame):  
    def __init__(self,parent,numberOfAnswers,response):
        tk.Frame.__init__(self,parent)
        
        self.ansSet = []
        for a in range(numberOfAnswers):
            self.ansSet.append(tk.IntVar())
            self.ansSet[a].set(a)

        self.width = int(math.sqrt(numberOfAnswers))
        self.buttonSet = []
        for i,item in enumerate(self.ansSet):
            self.buttonSet.append(tk.Button(self,textvariable=item,command=lambda item=item:response(item.get())))
            self.buttonSet[i].grid(row=int(math.floor(i/self.width)),column=int(i%self.width))    
        
    def updateAnsSet(self,newAnswers):
        for a,b in zip(self.ansSet,newAnswers):
            a.set(b)

def main():            
    #generate root
    root = tk.Tk()
    #attach mainFrame
    mainFrame = tk.Frame(root)
    mainFrame.pack(side='top')
    #create questionFrame
    qFrame = questionFrame(mainFrame)
    qFrame.pack(side='top')
    #create Quizmaster to handle question generation and answer checking
    qm = qg.QuizMaster()
    #This is the main callback function used by the buttons
    def responseA(answer):
        if not qm.checkAnswer(answer):
            tkMessageBox.Message(icon='info'
                    ,type='ok'
                    ,message=qm.answers['answer']).show()
            
        qm.createQuestion()
        qFrame.updateQuestion(qm.q1,qm.q2)
        aFrame.updateAnsSet(qm.handoverAnswers())

    #create answerFrame
    aFrame = answerFrame(mainFrame,4,responseA)
    aFrame.pack(side='top')    

    def quit(event=None):
        root.destroy()

    root.bind('<q>',quit)

    def show(event=None):
        qm.showSkill()

    root.bind('<s>',show)

    root.mainloop()

if __name__ == '__main__':
    main()

