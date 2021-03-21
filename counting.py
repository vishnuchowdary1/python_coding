counts = dict()
text = input('enter the text:')
line = open(text)
for a in line :
    words = a.split()
    #print(words)
    for word in words :
        counts[word] = counts.get(word,0) + 1
#print(counts)
bigcount = None
bigword = None
for k,v in counts.items():
    if bigcount is None or v > bigcount :
        bigword = k
        bigcount = v
print(bigword,bigcount)
