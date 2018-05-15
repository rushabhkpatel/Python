
def BinarySearchIterative(a, l, d, key):
	while(l <= d):
		mid = int(l + (d - l)/ 2)
		print(mid,l,d)
		if(array[mid] == key):
			return mid+1
		elif(array[mid] < key):
			l = mid+1
		else :
			d = mid-1	
	return -1

def BinarySearchRecursive(a, l, d, key):
	if(l > d) :
		return -1
	mid = int(l + (d - l)/ 2)
	if(a[mid] == key):
		return mid+1
	elif(a[mid] < key):
		return BinarySearchRecursive(a,mid+1,d,key)
	else:
		return BinarySearchRecursive(a,l,mid-1,key)

print("Enter the size of the array : ")
n = int(input())
print(n) 
print("Enter {} elements".format(n))
array = list(map(int,input().strip().split()))

for i in range(0, n) :
	print(array[i], end=" ")

print("\nEnter the element to search for : ")
key = int(input())
print(f"The element {key} is at {BinarySearchRecursive(array,0,n-1,key)}")


