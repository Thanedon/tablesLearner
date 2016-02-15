import qaFrames as qa
import qGen as qg
import Tkinter as tk

class QuizScreen(tk.Frame):
    def __init__(self,parent,type='typed'):
        
        tk.Frame.__init__(self,parent)
        self.pack(side='top')

        qFrame = qa.QuestionFrame(self)
        qFrame.pack(side='top')

        qm = qg.QuizMaster(qFrame)
        qm.nextQuestion()

        if type == 'typed':
            aFrame = qa.TypedResponseAnswerFrame(self,qm)
            aFrame.pack(side='top')
        else:
            aFrame = qa.MultiChoiceAnswerFrame(self,qm)
            aFrame.pack(side='top')

#class WelcomeScreen(tk.Frame):
#    def __init__(self,parent):
#        tk.Frame.__init__(self,parent)
#        self.pack(side='top')
#        
#        welcomeText = tk.Text(self,text='Press any button')
#        welcomeText.bind('<Key>',moveToNextScreen)

if __name__ == '__main__':
    
    root = tk.Tk()
    ag = QuizScreen(root)

    def quit(event=None):
        root.destroy()

    root.bind('<q>',quit)

    root.mainloop()


        
        

