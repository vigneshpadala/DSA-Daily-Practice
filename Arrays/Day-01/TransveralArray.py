#Traversal Arrays common sub-patterns
#1.Finding Max/min Elements in Array
#Taking  Array

arr=[3,25,8,4,5]

#1.finding max element
max_val=arr[0]
for i in range(1,len(arr)):
    if arr[i]>max_val:
        max_val=arr[i]
        print("max value:",max_val)


#2.sum of elements
total=0
for i in range(1,len(arr)):
    total+=arr[i]
print("sum of Array:",total)


#3.counting patterns(counting even numbers)
count=0
for i in range(1,len(arr)):
    if arr[i]%2==0:
       count+=1
print("counting even numbers:",count)


#4.check condition pattern(or Flag pattern)
#checking whether Array is sorted or unsorted Array
is_sorted=True
for i in range(1,len(arr)):
    if arr[i]<arr[i-1]:
        is_sorted=False
        break
print("is_sorted:",is_sorted)


#5.find Elements pattern(linear search)
target=25
found=False
for i in range(1,len(arr)):
    if arr[i]==target:
        found=True
        break

#find sorted or not
print("found:",found)

#find index number
print("index of target:",i)
