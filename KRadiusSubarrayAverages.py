def getAverages(nums, k):
    avg = []
    n = len(nums)
    windowLength = 2 * k + 1

    if n < windowLength:
        return [-1 for _ in range(n)]
    
    window = 0

    for i in range(k):
        avg.append(-1)
        window += nums[i] + nums[k + i]

    for i in range(k, n - k):
        window += nums[i + k]
        avg.append(window // windowLength)
        window -= nums[i - k]

    for i in range(n-k, n):
        avg.append(-1)

    return avg

if __name__ == '__main__':
    myNums= [7,4,3,9,1,8,5,2,6]
    myK = 3
    print(getAverages(myNums, myK))


"""
The values of indices < k are set to -1
The values of indices > len(nums) - k are also set to -1

Then the middle values are solved.
Keep a running sum of the current window and each time the
window moves, subtract the exiting number and add the new number.

"""