def minCost(nums, cost):
    pairs = [list(x) for x in sorted(zip(nums, cost))]
    totalCost = 0
    
    while len(pairs) > 1:
        # Identify which end of "pairs" has the lower cost
        if pairs[0][1] < pairs[-1][1]:
            # Merge the lowest value into the second lowest value
            totalCost += (pairs[1][0] - pairs[0][0]) * pairs[0][1]
            pairs[1][1] += pairs[0][1]
            pairs.pop(0)
        else:
            # Merge the higest value into the second highest value
            totalCost += (pairs[-1][0] - pairs[-2][0]) * pairs[-1][1]
            pairs[-2][1] += pairs[-1][1]
            pairs.pop(-1)

    return totalCost


if __name__ == '__main__':
    testNums = [1,3,5,2]
    testCost = [2,3,1,14]
    print(minCost(testNums, testCost))


"""
- Sort the nums array and then merge the values at the ends towards the
middle
- If the lowest value in the nums array has a lower cost than the higest
value, then merge it into the second lowest num in the array. Otherwise
merge the higest into the second highest
- Update the cost of the newly merged value to be the sum of the merged
values
- Keep a running tally of the total cost and add to it each time a merge
occurs

"""
