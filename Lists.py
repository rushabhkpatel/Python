#Lists in Python

numbers = [5,9,3,2,1,3,1]

print(type(numbers))

length = len(numbers)

print(length)

for i in numbers :
	print(i, end = " ")

print()

# Slicing

print(numbers[1 : 5]) #First index inclusive, but not the second one

print(numbers[ : 5])  #Default it takes starting of the list ie 0

print(numbers[2 : ]) #Default it takes end of the list, ie length - 1

#Built in methods for lists

numbers.append(10) #Adds 10 at the end of the list

print(numbers)

numbers.insert(2, 15) #Inserts at a particular position. arg1 - position arg2 - element to be inserted

print(numbers)

another_list = [11, 12, 13]

numbers.extend(another_list)

print(numbers)

#remove

numbers.remove(11)

print(numbers)

numbers.pop()  #Returns the element, can be captured in a variable

print(numbers)

numbers.reverse() #Reverses the list

print(numbers)

numbers.sort() #Sorts the list

print(numbers)

numbers.sort(reverse = True) #Sorts the list in Decreasing order

print(numbers)

#If we don't want to change the original list and just want to create a new list, Use the "sorted" function

numbersSortedList = sorted(numbers) #Returns a sorted list 

print(numbersSortedList)

print(str(min(numbers)) + " " + str(max(numbers)) + " " + str(sum(numbers))) 

