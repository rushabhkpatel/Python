#Learning to code in Python - DataType List
#Written by Rushabh Patel
#02-10-2017


print("Different data types in python" )
print("Just trying out something")
print("\n")
#print("NEWWWW")

#Creating a list :

grocery_list = ["Apple","Orange","Mango"]

#Printing an element in the list and modifying the element
print(grocery_list[1] + "\n")
grocery_list[0] = "Strawberry"
'''
#This is a for loop in python

for i in grocery_list :
    print(i)
'''
another_list = ["keyboard","Mouse", "Monitor"]

appended_list = grocery_list + another_list
grocery_list.extend(another_list) 
print(appended_list)
print(grocery_list)

# 	 Both the '+' and .extend() function do the same operation
#    .append() adds a list as a element of the outer list 
'''for i in grocery_list :
    print(i)

print("\n This is the first 3 elements of the appended list :", appended_list[:3])
'''


another_list.append("speakers")
print(another_list ,"\n")



