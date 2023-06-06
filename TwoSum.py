def twoSum(nums, target):
    numDict = {}
    for i in range(len(nums)):
        if nums[i] == target / 2:
            if target // 2 in numDict:
                return [i, numDict[target // 2]]
        numDict[nums[i]] = i

    for key, value in numDict.items():
        if target - key in numDict and numDict[target - key] != value:
            return[value, numDict[target - key]]
        
    return "Something went wrong"
        

if __name__ == '__main__':
    testNums = [3, 3]
    testTarget = 6
    print(twoSum(testNums, testTarget))
