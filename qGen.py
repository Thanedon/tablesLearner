import random as rd

def answerGen(first,second,num):
    trueAnswer = first * second
    dummyAnswers = [trueAnswer + rd.randint(-first,second) for x in range(num)] 
    return {'answer': trueAnswer, 'dummy': dummyAnswers}

class QuizMaster:
    def __init__(self,generator=answerGen):
        self.gen = generator
        self.firstRange = [13,19]
        self.secondRange = [17,19]

    def createQuestion(self):
        self.q1 = rd.randint(self.firstRange[0],self.firstRange[1])
        self.q2 = rd.randint(self.secondRange[0],self.secondRange[1])
        self.answers = self.gen(self.q1,self.q2,3)

    def changeRange(self,n1,n2):#,n3,n4):
        self.firstRange = [n1,n2] 
        #self.secondRange = [n3,n4]

    def checkAnswer(self,answer):
        if answer == self.answers['answer']:
            return True
        else:
            return False
    
    def handoverAnswers(self):
        answerList = self.answers['dummy'] + [self.answers['answer']]
        rd.shuffle(answerList)
        return answerList 


if __name__ == '__main__':
    
    qm = QuizMaster()
    qm.createQuestion()
    answers = qm.handoverAnswers()
    print answers
    #first = input('one number: ')
    #qm.changeRange(first,14)
    #while(1):
    #    qm.createQuestion()
    #    print 'what is ', qm.q1,'x',qm.q2
    #    second = input('answer?')
    #    print qm.checkAnswer(second)
        
