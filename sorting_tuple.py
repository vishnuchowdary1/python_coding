d = {'a':1,'b':35,'c':22,'d':12}
l = list()
for k,v in d.items() :
    l.append((v,k))
print(l)
print(sorted(l))
print(sorted(l, reverse=True))
