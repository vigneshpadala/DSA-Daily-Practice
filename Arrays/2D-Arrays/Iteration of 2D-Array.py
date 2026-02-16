def matrix_array(arr,m,n):
    for i in range(m):
        for j in range(n):
            print(arr[i][j],end=" ")
        print("")
    
    
arr=[[1,2,3],
     [4,5,6],
     [7,8,9]
     ]
m=n=3
print(matrix_array(arr,m,n))
