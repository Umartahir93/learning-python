(x,y)=('Umar','Tahir')
print(x)

(x,y) =('NBS','CDK')
print(x)

fhandle = open('countingwordsexample.txt')
count = dict()
for line in fhandle:
    words = line.split()
    for word in words:
        count[word] = count.get(word,0) +1


lst = list()
for key,value in count.items():
    newtuple=(value,key)
    lst.append(newtuple)

lst = sorted(lst,reverse=True)
for val,key in lst[:10]:
    print(key,val)


