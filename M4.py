# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 10:04:02 2023

@author: trent
"""
#clollection of random facts from the destiny series. credits to my freinds for info
questions = {"quest1":{"quest":"",
             "choices":["1)","2)","3)","4)"],
             "answer":"2)" },
             
             "quest2":{"quest":"placeholder",
             "choices":["1)","2)","3)","4)"],
             "answer":"2)" },
             
             "quest3":{"quest":"placeholder",
             "choices":["1)","2)","3)","4)"],
             "answer":"2)" },
             
             "quest4":{"quest":"placeholder",
             "choices":["1)","2)","3)","4)"],
             "answer":"2)" },
             
             "quest5":{"quest":"placeholder",
             "choices":["1)","2)","3)","4)"],
             "answer":"2)" },
             
             "quest6":{"quest":"placeholder",
             "choices":["1)","2)","3)","4)"],
             "answer":"2)" },
             
             "quest7":{"quest":"placeholder",
             "choices":["1)","2)","3)","4)"],
             "answer":"2)" },
             
             "quest8":{"quest":"placeholder",
             "choices":["1)","2)","3)","4)"],
             "answer":"2)" },
             
             "quest9":{"quest":"placeholder",
             "choices":["1)","2)","3)","4)"],
             "answer":"2)" },
             
             "quest10":{"quest":"placeholder",
             "choices":["1)","2)","3)","4)"],
             "answer":"2)" },
             
             "quest11":{"quest":"placeholder",
             "choices":["1)","2)","3)","4)"],
             "answer":"2)" },
             
             "quest12":{"quest":"placeholder",
             "choices":["1)","2)","3)","4)"],
             "answer":"2)" },
             
             "quest13":{"quest":"placeholder",
             "choices":["1)","2)","3)","4)"],
             "answer":"2)" },
             
             "quest14":{"quest":"placeholder",
             "choices":["1)","2)","3)","4)"],
             "answer":"2)" },
             
             "quest15":{"quest":"placeholder",
             "choices":["1)","2)","3)","4)"],
             "answer":"2)" },
             
             "quest16":{"quest":"placeholder",
             "choices":["1)","2)","3)","4)"],
             "answer":"2)" },
             
             "quest17":{"quest":"placeholder",
             "choices":["1)","2)","3)","4)"],
             "answer":"2)" },
             
             "quest18":{"quest":"placeholder",
             "choices":["1)","2)","3)","4)"],
             "answer":"2)" },
             
             "quest19":{"quest":"placeholder",
             "choices":["1)","2)","3)","4)"],
             "answer":"2)" },
             
             "quest20":{"quest":"placeholder",
             "choices":["1)","2)","3)","4)"],
             "answer":"2)" }
             }
i = 0
incorTally = 0
v = 0
corQues = 0
for i in questions:
    v = v + 1
    print('Question ' + str(v) + ": ", questions[i]['quest'])
    for b in questions[i]['choices']:
        print(b + " ",end ="") 
    print()
    print('what is the answer?: ')
    guess = input()
    answer = questions[i]['answer']
    if guess == answer:
        print('correct!')
        print()
        corQues = corQues + 1
    else:
        print('incorrect the answer was', questions[i]['answer'])
        print()
        incorTally = incorTally + 1
        if incorTally == 3 :
            print('You lose!')
            break
if corQues > 17:
    print('You win!')
print('Correct questions: ', corQues)
print('Incorrect questions: ', incorTally)
