import random as rd
import tkMessageBox

def answerGen(first,second,num):
    return [first*second + rd.randint(-first,second) for x in range(num)]

class QuizMaster:
    def __init__(self,qFrame):
        self.firstRange = [3,19]
        self.secondRange = [13,19]
        self.qFrame = qFrame

    def nextQuestion(self):
        self.q1 = rd.randint(self.firstRange[0],self.firstRange[1])
        self.q2 = rd.randint(self.secondRange[0],self.secondRange[1])
        self.answer = self.q1*self.q2
        return self.q1,self.q2

    def checkAnswer(self,answer):
        return answer == self.answer

    def receiveAnswer(self,answer,aFrame):
        if not self.checkAnswer(answer):
            #this messagebox feels like it's in the wrong place
            tkMessageBox.Message(icon='info',type='ok',message=self.answer).show()
        self.qFrame.updateQuestion(self.nextQuestion())
        aFrame.refresh()
    
def main():    
    pass
        
if __name__ == '__main__':
    main()
