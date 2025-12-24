class MoveZeroes:
    def __init__(self, arr):
        self.arr = arr

    def move_zeroes_to_end(self):
        pos = 0  # position for next non-zero element

        for i in range(len(self.arr)):
            if self.arr[i] != 0:
                # swap
                self.arr[pos], self.arr[i] = self.arr[i], self.arr[pos]
                pos += 1

        return self.arr


# Driver code
if __name__ == "__main__":
    arr = [0, 1, 0, 3, 12]
    obj = MoveZeroes(arr)
    result = obj.move_zeroes_to_end()
    print("Array after moving zeroes:", result)
    
