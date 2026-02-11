# Const_time_complexity:
# O(1)-Always takes the same time
def const_time_example(arr):
    return arr[0]

# Linear_time_complexity:
# O(n)-Grows linearly with input size
def linear_time_example(arr):
    for i in range(len(arr)):
        print(arr[i])

# Quadratic_time_complexity:
# O(n2)-Grows Quadratically with nested loops
def quadratic_time_example(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i],arr[j])

# Logarithmic_time_complexity
# O(log n)-Grows slowly, cutting the problem in half each time
def logarithmic_time_example(arr,target):
    l=0
    r=len(arr)-1
    while l<=r:
        mid=l+r//2
        if target==arr[mid]:
            return mid
        elif target>arr[mid]:
            l+=1
        else:
            r-=1

# Exponential_time_complexity:
# O(2n)-Grows Exponentially, doubling the work at every step
def exponential_time_example(n):
    if n==0 or n==1:
        return 1
    return exponential_time_example(n-1)+exponential_time_example(n-2)

arr=[0,1,2,3,4]
print(const_time_example(arr))
print(linear_time_example(arr))
print(quadratic_time_example(arr))
target=3
print(logarithmic_time_example(arr,target))
n=5
print(exponential_time_example(n))
