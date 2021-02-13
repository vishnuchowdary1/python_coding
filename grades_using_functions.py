value = input('enter your grade: ')
try :
    grade = float(value)
except :
    print('Bad Score')

def computegrade(grade) :
    if grade >= 1 :
        return 'Bad Score'
    if grade >= 0.9 :
        return 'A'
    if grade >= 0.8 :
        return 'B'
    if grade >= 0.7 :
        return 'C'
    if grade >= 0.6 :
        return 'D'
    else :
        return 'F'
try:
    print(computegrade(grade)) 
except :
    print('please enter valid score')   