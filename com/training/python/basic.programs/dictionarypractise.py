names =["candy","biscuits","juice","candy","biscuits","juice"]
counts = dict()

for name in names:
    counts[name] =counts.get(name,0) +1

print(counts)

counts = dict()

for name in names:
    if name in counts:
        counts[name] = counts[name]+1
    else:
        counts[name] = 1

print(counts)


# counting from file
filehandle = open("countingwordsexample.txt")
text = filehandle.read().strip()
words = text.split()
counts = dict()
for word in words:
    counts[word] = counts.get(word,0)+1

print(counts)

#loop with dictionary
for key in counts:
    print(key , counts[key])


#maximum word and maximum count
bigWord = None
bigCount = None

for key,value in counts.items():
    if bigWord is None or value > bigCount:
        bigWord = key
        bigCount = value

print("The word :",bigWord,"Biggest Count",bigCount)