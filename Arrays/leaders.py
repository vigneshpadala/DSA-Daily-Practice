def leaders(arr):
  n=len(arr)
  result=[]
  for i in range(0,n):
    for j in range(i+1,n):
      if arr[i]<arr[j]:
        break
    else:
      print(result.append(arr[i]))
  return result
  

if __name__ == "__main__":
    arr = [16, 17, 4, 3, 5, 2]
    result = leaders(arr)
    print(" ".join(map(str, result)))
