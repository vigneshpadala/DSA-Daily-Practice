class Moveduplicates:
    def __init__(self, arr):
        self.arr = arr

    def move_duplicates(self):
        s1=[]
        for f in range(len(self.arr)):
            if self.arr[f] in s1:
                continue
            else:
                 s1.append(self.arr[f])
        return s1


# Driver code
if __name__ == "__main__":
    arr = [0,0,1,1,2,3,3,3,4,4,5,5]
    obj = Moveduplicates(arr)
    result = obj.move_duplicates()
    print("Array after moving duplicates:", result)
