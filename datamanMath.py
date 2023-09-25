#make module importable
def mathParse(stri):
    b = 0
    new = False
    mathprep = ['']
    i = 0
    for i in stri:
        if i.isalpha():
            break;
        elif i.isnumeric():
            if new == True:
                b = b + 1
                mathprep.append(i)
                new = False
            else:
                mathprep[b] = mathprep[b] + i
        elif (i=='+' or i=='-' or i== '/' or i=='*'):
            b = b + 1
            new = True
            mathprep.append(i)
    return mathprep

def mathDo(preped):
    while len(preped) != 1:
        b = 0
        for i in preped:
            if( i == '*' ):
                 pos1 = b-1
                 pos2 = b+1
                 numOne = float(preped[pos1])
                 numTwo = float(preped[pos2])
                 preped[pos1+1] = mult(numOne,numTwo )
                 del preped[pos1]
                 del preped[pos2-1]
            b = b + 1
        b = 0
        for i in preped:
            if( i == '/' ):
                 pos1 = b-1
                 pos2 = b+1
                 numOne = float(preped[pos1])
                 numTwo = float(preped[pos2])
                 preped[pos1+1] = dev(numOne,numTwo )
                 del preped[pos1]
                 del preped[pos2-1]
            b = b + 1
        b = 0
        for i in preped:
            if( i == '+' ):
                 pos1 = b-1
                 pos2 = b+1
                 numOne = float(preped[pos1])
                 numTwo = float(preped[pos2])
                 preped[pos1+1] = add(numOne,numTwo )
                 del preped[pos1]
                 del preped[pos2-1]
            b = b + 1
        b = 0
        for i in preped:
            if( i == '-' ):
                 pos1 = b-1
                 pos2 = b+1
                 numOne = float(preped[pos1])
                 numTwo = float(preped[pos2])
                 preped[pos1+1] = sub(numOne,numTwo )
                 del preped[pos1]
                 del preped[pos2-1]
            b = b + 1
        return preped

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

def main():
    egg = input()
    eeg = mathParse(egg)
    print(eeg)
    gee = mathDo(eeg)
    print(gee)
    
#only run main if not import
if __name__ == '__main__':
    main()
    print(17*9+23-2/6)
