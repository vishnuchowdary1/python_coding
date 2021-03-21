a = dict()
names = ['a','b','c','d','e','d']
for name in names:
    a[name] = a.get(name,0) + 1
    #print (a)
print(a)
