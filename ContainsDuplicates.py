def containsDuplicate(nums):
    numSet = set(nums)
    return len(nums) != len(numSet)
