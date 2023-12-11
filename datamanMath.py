#make module importable
def mathParse(stri):
    b = 0
    new = False
    mathprep = ['']
    i = 0
    dotCon = 0
    fail = "2"
    for i in stri:
        if i.isalpha():
            fail = "Letter error."
            break;
        elif i.isnumeric() or i=='.':
            if new == True:
                dotCon = 0
                b = b + 1
                mathprep.append(i)
                new = False
            else:
                mathprep[b] = mathprep[b] + i
                if i == ".":
                    dotCon = dotCon + 1
                    if dotCon == 2:
                        fail = "Period after peroid error."
                        break;
                    
        elif (i=='+' or i=='-' or i== '/' or i=='*'):
            b = b + 1
            new = True
            mathprep.append(i)
    return mathprep, fail

def mathDo(preped):
    while len(preped) != 1:
        b = 0
        rerun = 0
        while rerun == 0:
            rerun = 1
            b = 0
            for i in preped:
                if( i == '*' ):
                    rerun = 0
                    pos1 = b-1
                    pos2 = b+1
                    numOne = float(preped[pos1])
                    numTwo = float(preped[pos2])
                    preped[pos1+1] = mult(numOne,numTwo )
                    del preped[pos1]
                    del preped[pos2-1]
                b = b + 1
        b = 0
        rerun = 0
        while rerun == 0:
            rerun = 1
            b = 0
            for i in preped:
                if( i == '/' ):
                    rerun = 0
                    pos1 = b-1
                    pos2 = b+1
                    numOne = float(preped[pos1])
                    numTwo = float(preped[pos2])
                    preped[pos1+1] = dev(numOne,numTwo )
                    del preped[pos1]
                    del preped[pos2-1]
                b = b + 1
        b = 0
        rerun = 0
        while rerun == 0:
            rerun = 1
            b = 0
            for i in preped:
                if( i == '+' ):
                    rerun = 0
                    pos1 = b-1
                    pos2 = b+1
                    numOne = float(preped[pos1])
                    numTwo = float(preped[pos2])
                    preped[pos1+1] = add(numOne,numTwo )
                    del preped[pos1]
                    del preped[pos2-1]
                b = b + 1
        b = 0
        rerun = 0
        while rerun == 0:
            rerun = 1
            b = 0
            for i in preped:
                if( i == '-' ):
                    rerun = 0
                    pos1 = b-1
                    pos2 = b+1
                    numOne = float(preped[pos1])
                    numTwo = float(preped[pos2])
                    preped[pos1+1] = sub(numOne,numTwo )
                    del preped[pos1]
                    del preped[pos2-1]
                b = b + 1
            outSolution = preped[0]
        return outSolution

# Addintion calculation
def add(numbOne, numbTwo):
    result = float(numbOne) + float(numbTwo)
    return result;

# Subtraction caclulation
def sub(numbOne, numbTwo):
    result = float(numbOne) - float(numbTwo)
    return result

# Multiplication calculation
def mult(numbOne, numbTwo):
    result = float(numbOne) * float(numbTwo)
    return result
# Devision calculation
def dev(numbOne, numbTwo):
    result = float(numbOne) / float(numbTwo)
    return result

def doMath(inEquation):
    outSolution = ""
    parsed, fail = mathParse(inEquation)
    if fail != "":
        outSolution = mathDo(parsed)
    return outSolution, fail
    
    

def main():
    go = 1
    while (go == 1):
        uinput = input("Enter your equasion:  ")
        solution, fail = doMath(uinput)
        if fail == "2":
            print(solution)
        else:
            print(fail)
        goAgain = input("would you like to do another equasion? y/n : ")
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
                goAgain = input("would you like to do another equasion? y/n : ")

def truncate(n, decimals = 0):
    multiplier = 10 ** decimals
    return n * multiplier / multiplier
    
#only run main if not import
if __name__ == '__main__':
    main()
