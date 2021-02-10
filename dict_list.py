fname = input('enter file name: ')
file = open(fname)
di = dict()
for line in file :
    line = line.rstrip()
    words = line.split()
    for word in words :
        # this is very imp prop in dictionaries 
        # it is like idiom which retrieves/creates/counts 
        di[word] = di.get(word,0) + 1
print(di)

# now find the most common word

bigword = None
bigcount = 0
for k,v in di.items() :
    if v > bigcount :
        bigcount = v
        bigword = k

print(bigword,bigcount)