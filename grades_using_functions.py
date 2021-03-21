lt = [9,2,5,3,7,6]
largest = 0
for x in lt :
    if x > largest :
        largest = x
print('largest:',largest)
smallest = None
for y in lt :
    if smallest is None or smallest > y :
        smallest = y 
print('smallest:',smallest)