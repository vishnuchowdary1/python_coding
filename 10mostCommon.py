name = input('enter file name: ')
file = open(name)
di = dict()
for lines in file :
    words = lines.split()
    for word in words:
        di[word] = di.get(word,0) + 1

li = list()
for k,v in di.items() :
    li.append((v,k))

li = sorted(li, reverse=True)
print(li[:10])

for v,k in li[:10] :
    print(k,v)
