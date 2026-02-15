# Intersection of two arrays:

def unique(arr1,arr2):
    return list(set(arr1) & set(arr2))
     
arr1=[2,1,2,1,3]
arr2=[1,4,2]
print(unique(arr1,arr2))
