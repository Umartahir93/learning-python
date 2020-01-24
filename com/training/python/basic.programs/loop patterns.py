#largest
largest_so_far = -1
for data in [21,23,31,421,1,2,3] :
    if data > largest_so_far:
        largest_so_far = data
        print("largest value until now" ,largest_so_far)

print("largest value at the end",largest_so_far)

#count
count = 0;

for data in [1,2,12,1,1,1]:
    count = count +1
print("count is ",count)

#sum
sum = 0
for data in [1,2,12,1,21,1]:
    sum = sum + data

print("total sum of loop",sum)

#average
sum = 0
count = 0
for data in [1,2,34,5,6,43,32]:
    count = count +1
    sum = sum+data
    print(count,sum,data)

print("Average of the number is ",sum/count)


#print values greater than 20
for data in [1,31,1,31,421,12]:
    if(data >20):
        print("Value greater than 20 ",data)


#smallest
smallest_so_far = None
for value in [1,2,3,4,5,6,7,-8]:

    if smallest_so_far is None:
        smallest_so_far = value
    elif value <smallest_so_far:
        smallest_so_far = value

    print("Smallest so far",smallest_so_far)

print("Smallest",smallest_so_far)


