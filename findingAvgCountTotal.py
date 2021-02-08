count = 0
total = 0
while True:
    v = input('Enter a number: ')
    if v == 'done':
        break
    try :
        val = float(v)
    except :
        print("Invalid Input")

    #print(val)
    count = count + 1
    total = total + val

print(count, total, total/count)
