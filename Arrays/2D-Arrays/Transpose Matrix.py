def matrix_array(arr,m,n):
    print("Matrix:")
    for i in range(m):
        for j in range(n):
            print(arr[i][j],end=" ")
        print("")
    print("Transpose Matrix:")
    for i in range(m):
        for j in range(n):
            print(arr[j][i],end=" ")
        print("")
    
    
arr=[[1,2,3],
     [4,5,6],
     [7,8,9]
     ]
m=n=3
print(matrix_array(arr,m,n))
