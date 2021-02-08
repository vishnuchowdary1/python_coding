def salary(h,r):
    if h > 40:
        ori = h*r
        ot = (h-40)*(r*0.5)
        sal = ori+ot
    else:
        sal = h*r
    return sal

hrs = input('enter hours worked:')
rate = input('enter rate:')
try:
    h = float(hrs)
    r = float(rate)
except:
    print('enter numerical value')
    quit()

print('pay per week:',salary(h,r))
