#FizzBuzz program - Python Implementation
#Written by Rushabh Patel
#15-10-2017

#FizzBuzz
# for 1 to n both inclusive
# 1. print Fuzz if mult of 3
# 2. print Buzz if mult of 5
# 3. print fizzBuzz if mult of both 3 and 5
# 4. otherwise print the number

n = int(input('Enter the end range : '))

for i in range(1, n+1) :
    if(i % 3 == 0 and i % 5 == 0) :
        print("fizzbuzz")
    elif(i % 3 == 0) :
        print("fizz")
    elif(i % 5 == 0) :
        print("buzz")
    else :
        print(i) 