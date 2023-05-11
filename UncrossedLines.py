def maxUncrossedLines(nums1, nums2, result=0):
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i] == nums2[j]:
                return max(maxUncrossedLines(nums1[i+1:], nums2,
                                result), maxUncrossedLines(nums1[i+1:],
                                nums2[j+1:], result+1))

    return result


if __name__ == '__main__':
    testNums1 = [19,5,19,19,2,9,5,19,20,17,3,1,7,10,19,16,8,3,13,13,16,3,16,7,14,11,18,5,8,12,8,15,18,10,8,8,12,8,9,17,17,14,14,1,8,19,8,1,5,4]
    testNums2 = [18,20,18,18,4,7,17,17,1,18,6,4,11,14,19,15,12,20,3,5,12,2,13,14,9,16,6,4,16,8,10,19,15,18,12,11,9,14,7,9,14,15,6,18,12,8,20,11,2,17]
    print(maxUncrossedLines(testNums1, testNums2))

"""
Maintain a pointer for the second array, pointing to the first number that 
hasn't been used yet.

Move through the first array and for each number check if there is a 
corresponding number in the second array. If there is, use recursion to
determine the outcome if:
- That number pair is used
- That number pair is ignored
"""
