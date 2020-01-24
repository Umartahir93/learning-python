#string letters
fruit = 'apple'
for letter in fruit:
    print(letter)


#string letters
fruit = 'guvava'
index = 0
while index < len(fruit):
    print(index,fruit[index])
    index = index+1

print(fruit[0:4])
print(fruit[:])

#school name program
schoolEmailAddress = 'Umar Tahir l135947@lhr.nu.edu.pk Lahore Yes'
indexOfAt =schoolEmailAddress.find('@')
indexOfSpacelName = schoolEmailAddress.find(' ', indexOfAt)

print(schoolEmailAddress[indexOfAt+1:indexOfSpacelName])


