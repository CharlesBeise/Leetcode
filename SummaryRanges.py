def summaryRanges(nums):
    if len(nums) == 0:
        return []
    else:
        summary = []
        cur = nums[0]
        count = 1

    for i in range(1, len(nums)):
        if nums[i] == cur + count:
            count += 1
        elif count == 1:
            summary.append(str(cur))
            cur = nums[i]
        else:
            summary.append(str(cur) + "->" + str(nums[i-1]))
            cur = nums[i]
            count = 1

    if count == 1:
        summary.append(str(cur))
    else:
        summary.append(str(cur) + "->" + str(nums[-1]))

    return summary


if __name__ == '__main__':
    myNums = [0,1,2,4,5,7]
    print(summaryRanges(myNums))
