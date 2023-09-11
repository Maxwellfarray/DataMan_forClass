#make module importable
def mathParse(str):
    b = 0
    new = False
    mathprep = ['']
    for i in str:
        print(i)
        if i.isalpha():
            print('please only enter math formula symbols and numbers')
            break;
        elif i.isnumeric():
            if new == True:
                b = b + 1
                mathprep.append(i)
            else:
                mathprep[b] = mathprep[b] + i
        elif (i=='+' or i=='-' or i== '/' or i=='*'):
            b = b + 1
            new = True
            mathprep.append(i)
    print(mathprep)        
    print("end")


egg = input()
mathParse(egg)


    