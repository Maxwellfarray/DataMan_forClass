import datamanMath as mMod
import random

def main():
    mathGame()
    # inTestInput = input()
    # testInput = mMod.doMath(inTestInput)
    # print(testInput)
    # inTestAnswer = float(input())
    # correct = compareQes(testInput,inTestAnswer)
    # print(correct)
    
def compareQes(inQuestionCorrAns, inAnswer):
    outRightWrong = inAnswer == inQuestionCorrAns
    return outRightWrong

def createQes(inNumbersAmount):
        outQuestion = []
        for i in range(inNumbersAmount):      
            outQuestion.append(str(random.randrange(1,100)))
            if i != inNumbersAmount - 1:
                control = random.randrange(3)
                if control == 3:
                    outQuestion.append('-')
                elif control == 2:
                    outQuestion.append('+')
                elif control == 1:
                    outQuestion.append('*')
                else:
                    outQuestion.append('/')  
        return outQuestion

def mathGame():
    outputQuestion = ''
    chalLev = int(input("Number of numbers: "))
    question = createQes(chalLev)
    for i in range(len(question)):
        outputQuestion = outputQuestion + question[i] + " "
    answer = mMod.doMath(question)
    print(mMod.truncate(answer,3))
    correct = False
    i = 0
    while correct == False:
        if i == 0:
            print(outputQuestion)
            attempt = input("Enter the answer the question above rounded to the next whole number: ")  
        else:
            attempt = input("wrong try again: ")
        i = i + 1
        correct = compareQes(mMod.truncate(answer,3), float(attempt))
    print("correct!")
        
        
        
if __name__ == '__main__':
    main()