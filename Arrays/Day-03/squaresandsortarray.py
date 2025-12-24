class squaresandsortedarray:
    def __init__(self, arr):
        self.arr = arr

    def square_sortedarray(self):
        l=[]
        for i in range(len(self.arr)):
            l.append(self.arr[i]*self.arr[i])

        l.sort()
        return l

# Driver code
if __name__ == "__main__":
    arr = [-4,-1,0,2,5]
    obj = squaresandsortedarray(arr)
    result = obj.square_sortedarray()
    print("Array after squares and sorted array:", result)

