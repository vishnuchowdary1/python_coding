value = input('enter the year:')
try :
    year = float(value)
except :
    print('Bad Value')
    exit()

def is_leap(year) :
    if year%400 == 0 :
        return 'True'
    elif year%100 == 0 :
        return 'False'
    elif year%4 == 0 :
        return 'True'
    else :
        return 'False'

print(is_leap(year))