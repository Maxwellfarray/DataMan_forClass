import datamanMath as mMod

def main():
    inTestInput = input()
    testInput = mMod.doMath(inTestInput)
    print(testInput)
    inTestAnswer = float(input())
    correct = compareQ(testInput,inTestAnswer)
    print(correct)
    
def compareQ(inQuestionCorrAns, inAnswer):
    outRightWrong = inAnswer == inQuestionCorrAns
    return outRightWrong
    

if __name__ == '__main__':
    main()

