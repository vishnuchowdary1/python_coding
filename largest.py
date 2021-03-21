a = input('enter file name:')
x = open(a,'r')
lst = list()
for line in x:
    word = line.rstrip().split()
    #print(word)
    for ele in word:
        if ele in lst:
            continue
        else:
            lst.append(ele)
lst.sort()
print(lst)
