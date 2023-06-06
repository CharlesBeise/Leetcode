def containsNearbyDuplicate(nums, k):
    if k >= len(nums):
        numSlice = set(nums)
    else:
        numSlice = set(nums[:k + 1])

    if len(nums[:k+1]) != len(numSlice):
        return True

    for i in range(k, len(nums)-1):
        numSlice.remove(nums[i-k])
        numSlice.add(nums[i+1])
        if len(numSlice) != k + 1:
            return True

    return False


if __name__ == '__main__':
    myNums = [1,2,3,1,2,3]
    myK = 2
    print(containsNearbyDuplicate(myNums, myK))
