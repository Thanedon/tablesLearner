


import Tkinter as tk
import qaFrames as qf


root = tk.Tk()

mainFrame = tk.Frame(root)
mainFrame.pack(side='top')

qFrame = qf.questionFrame(mainFrame)

aFrame = qf.answerFrame(mainFrame,4)


root.mainloop()

