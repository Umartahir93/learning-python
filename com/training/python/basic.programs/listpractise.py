things = list()
things.append("car")
things.append("dog")
things.append("computer")
things.append("resume")
things.sort()
print(things)


avergaeList = list()
while True:
    num = input("Enter a number ")
    if num == "done": break
    num = float(num)
    avergaeList.append(num)


print(sum(avergaeList)/len(avergaeList))

line = "A lot of list methods"
wordList = line.split()
print(wordList)

line = "thing;car;television"

print(line.split(";"))

filehandler = open("email.txt")
for line in filehandler:
    line = line.strip()
    if not line.startswith("From "): continue
    words= line.split()
    print(words[2])

lists=[]
lists.append("1231233213")
print(lists)




