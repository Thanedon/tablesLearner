import Tkinter as tk
import qaFrames as qf
import qGen as qg


root = tk.Tk()

mainFrame = tk.Frame(root)
mainFrame.pack(side='top')

qFrame = qf.questionFrame(mainFrame)
qFrame.pack(side='top')

qm = qg.QuizMaster()

aFrame = qf.answerFrame(mainFrame,4)
aFrame.pack(side='top')

root.mainloop()

