number = "153"
power = int(len(number))
#print(power)
new_no = 0
for i in number :
    a = int(i) ** power
    new_no = new_no + a
print(new_no)

if int(number) == new_no :
    print('True')
else :
    print('False')