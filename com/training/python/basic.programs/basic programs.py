# first practise paragraph
print('Hello World')

#second practise paragraph
userinput = input("Which floor?")
print("floor in eurpoe",userinput)

#third practise paragraph
userinput = int(userinput)+1
print("floor in USA",userinput)


#fourth practise paragraph
x = 4
if x > 2:
    print('greater')
else :
    print('smaller')

print ('all donne')


#fifth practise paragraph
if x == 1 :
    print("its equal")

elif x > 1 :
    print("x greater than 1")

elif x >= 3:
    print("blah blah blah")

else :
    print("hmmm")


#fifth practise paragraph
rawstr = input("Enter the number to check")
try:
    ival = int(rawstr)
except:
    ival = -1

if ival >  0 :
    print("Nice work")
elif ival < 0:
    print("Please enter number not a string")


#sixth practise paragraph
inputString = "HelloWorld"
bigLetter = max(inputString)
smallLetter = min(inputString)
print("Maximum letter in String",bigLetter)
print("Minimum letter in String",smallLetter)


#SEVENTH PRACTISE PARAGRAPH
def greet(lang):
    if lang == "en" :
        return "Hello"
    elif lang == "es" :
        return "OLA"
    elif lang == "pu" :
        return "ke haal hai"
    else :
        return "so many retuns are just for practise"



print(greet("pu"), "practise")





