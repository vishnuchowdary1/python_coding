hours=input('enter your hours:')
rate=input('enter rate per hour:')
try:
    h=float(hours)
    r=float(rate)
except:
    print('please enter numerical')
    quit()

if h<=40:
    amt=h*r
    print(amt)
else:
    amt=h*r
    ot=(h-40)*(r*1.5)
    amount=amt+ot
    print(amount)
