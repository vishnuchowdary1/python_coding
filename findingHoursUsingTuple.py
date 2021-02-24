name = input('enter file name: ')
handle = open(name)
dit = dict()
for line in handle :
    if not line.startswith('From') :
        continue
    else :
        words = line.rstrip().split()
        if len(words) > 3 :
            word = words[5]
            #print(word)
            word = word[0:2]
            #print(word)
            dit[word] = dit.get(word,0) + 1
        else :
            continue
#print(dit)
lt = list()
for k,v in dit.items() :
    lt.append((k,v))
lt = sorted(lt)
#print(lt)
for k,v in lt:
    print(k,v)