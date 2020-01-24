# read whole file as sequance of all characters
inputFileHandle = open('InputFileForReading.txt') #gives you handle
inputFile = inputFileHandle.read()
print(len(inputFile))

#count lines
inputFileHandle = open('InputFileForReading.txt') #gives you handle
count = 0
for line in inputFileHandle: #Read file using handle
    count = count+1;
print(count)


#searching through the line
inputFileHandle = open('InputFileForReading.txt') #gives you handle
for line in inputFileHandle:
    if line.startswith("Hi"):
        print(line.rstrip())


#skipping through the line
inputFileHandle = open('InputFileForReading.txt') #gives you handle
for line in inputFileHandle:
    if line.startswith("Hi"):
        continue
    print(line.rstrip())


