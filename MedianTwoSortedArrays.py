def findMedianSortedArrays(nums1, nums2):
    i = j = k = 0

    maxLength = len(nums1) + len(nums2)

    midpoint = maxLength // 2

    if maxLength % 2 == 0:
        midpoint -= 1

    while i < len(nums1) and j < len(nums2) and k < midpoint:
        if nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
        k += 1

    if i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            median = nums1[i]
            i += 1
        else:
            median = nums2[j]
            j += 1
    elif i < len(nums1):
        i += midpoint - k + 1
        median = nums1[i - 1]
    else:
        j += midpoint - k + 1
        median = nums2[j - 1]


    # If there are an even number of numbers
    if maxLength % 2 == 0:
        if i < len(nums1):
            if j < len(nums2):
                median = (median + min(nums1[i], nums2[j])) / 2
            else:
                median = (median + nums1[i]) / 2
        else:
            median = (median + nums2[j]) / 2

    return median


def findMedianSortedArrays1(nums1, nums2):
    i = j = 0

    someNums = []

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            someNums.append(nums1[i])
            i += 1
        else:
            someNums.append(nums2[j])
            j += 1

    while i < len(nums1):
        someNums.append(nums1[i])
        i += 1

    while j < len(nums2):
        someNums.append(nums2[j])
        j += 1

    numLength = len(someNums)

    if numLength % 2 == 0:
        return (someNums[numLength//2] + someNums[(numLength//2) - 1]) / 2
    else:
        return someNums[(numLength//2)]



if __name__ == '__main__':
    myNums1 = [1,3]
    myNums2 = [2,4]
    print(findMedianSortedArrays(myNums1, myNums2))
