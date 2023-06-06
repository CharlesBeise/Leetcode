def canMakeArithmeticProgression(arr):
    def sortList(nums):
        if len(nums) < 2:
            return nums

        # Split the array in half and sort each half
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        sortList(left)
        sortList(right)

        # Merge the two halves
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

        return nums

    arr = sortList(arr)

    dif = arr[1] - arr[0]

    for i in range(2, len(arr)):
        if arr[i] - arr[i-1] != dif:
            return False

    return True


if __name__ == '__main__':
    myArr = [1,3,5,2,4,9]
    print(canMakeArithmeticProgression(myArr))
