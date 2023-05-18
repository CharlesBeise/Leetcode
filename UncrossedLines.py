def maxUncrossedLines(nums1, nums2):
    dp = [[0 for _ in range(len(nums1) + 1)] for _ in range(len(nums2) + 1)]

    for i in range(1, len(nums1) + 1):
        for j in range(1, len(nums2) + 1):
            if nums1[i-1] == nums2[j-1]:
                dp[j][i] = dp[j-1][i-1] + 1
            else:
                dp[j][i] = max(dp[j-1][i], dp[j][i-1])

    return dp[-1][-1]


if __name__ == '__main__':
    testNums3 = [19,5,19,19,2,9,5,19,20,17,3,1,7,10,19,16,8,3,13,13,16,3,16,7,14,11,18,5,8,12,8,15,18,10,8,8,12,8,9,17,17,14,14,1,8,19,8,1,5,4]
    testNums4 = [18,20,18,18,4,7,17,17,1,18,6,4,11,14,19,15,12,20,3,5,12,2,13,14,9,16,6,4,16,8,10,19,15,18,12,11,9,14,7,9,14,15,6,18,12,8,20,11,2,17]
    testNums1 = [1, 4, 2]
    testNums2 = [1, 2, 4]
    print(maxUncrossedLines(testNums3, testNums4))

"""
Create a matrix to hold values which represent solutions for subproblems of the
original problem, initialized to zero, then solve using a bottom-up approach.
"""
