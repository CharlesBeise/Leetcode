def merge(nums1, m, nums2, n):
    if n == 0:
        return nums1
    elif m == 0:
        for i in range(n):
            nums1[i] = nums2[i]
        return nums1
    
    i = j = 0
    temp = []

    while i < m and j < n:
        if nums1[i] < nums2[j]:
            temp.append(nums1[i])
            i += 1
        else:
            temp.append(nums2[j])
            j += 1

    while i < m:
        temp.append(nums1[i])
        i += 1
    
    while j < n:
        temp.append(nums2[j])
        j += 1

    for i in range(m+n):
        nums1[i] = temp[i]

    return nums1



if __name__ == '__main__':
    testNums1 = [4,5,6,0,0,0]
    testM = 3
    testNums2 = [1,2,3]
    testN = 3
    print("test")
    print(merge(testNums1, testM, testNums2, testN))
