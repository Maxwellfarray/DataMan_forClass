import datamanMath as mMod
import random
import csv

def main():
    go = 1
    while go == 1:
        mathGame()
        goAgain = input("would you like to answer another question? y/n : ")
        goie = 1
        while goie == 1:
            if goAgain == 'y':
                print('ok')
                goie = 0
            elif goAgain == 'n':
                print("exiting caculator")
                go = 0
                goie = 0
            else:
                print("please only enter the given oprions.")
                goAgain = input("would you like to answer another question? y/n : ")
    
    
def writer(headerIn,trasactionDicIn):
    with open('quesrec.csv', 'w',newline='') as csvfile:
        header = []
        writer = csv.DictWriter(csvfile, fieldnames = headerIn)
        accumulator = []
        for item in trasactionDicIn.values():
            accumulator.append(item)  
        writer.writeheader()
        writer.writerows(accumulator)
    
def compareQes(inQuestionCorrAns, inAnswer):
    outRightWrong = inAnswer == inQuestionCorrAns
    return outRightWrong

def createQes(diff,leng):
        outQuestion = []
        for i in range(leng): 
            outQuestion.append(str(random.randrange(1,diff*10)))
            if diff == 1:
                if i != leng - 1:
                    control = random.randrange(2)
                    if control == 1:
                        outQuestion.append('-')
                    else:
                        outQuestion.append('+') 
            else:
                if i != leng - 1:
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
    chalLev = int(input("Enter difficulty of questions: "))
    leng = int(input("Enter length of questions."))
    question = createQes(chalLev,leng)
    for i in range(len(question)):
        outputQuestion = outputQuestion + question[i] + " "
    answer,fail = mMod.doMath(question)
    print(mMod.truncate(int(answer),3))
    correct = False
    i = 0
    while correct == False:
        if i == 0:
            print(outputQuestion)
            attempt = input("Enter the answer the question above : ")
        else:
            attempt = input("wrong try again: ")
        i = i + 1
        correct = compareQes(mMod.truncate(int(answer),3), float(attempt))
    print("correct!")
        
        
        
if __name__ == '__main__':
    main()