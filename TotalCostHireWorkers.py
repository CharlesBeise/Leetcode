import bisect


def totalCost(costs, k, candidates):
    workers = len(costs)
    total = 0

    if workers <= candidates * 2:
        costs.sort()
        for i in range(k):
            total += costs[i]
        return total

    i = 0
    front = []
    end = []

    for _ in range(candidates):
        bisect.insort_right(front, costs.pop(0))
        bisect.insort_right(end, costs.pop(-1))

    # Hire workers this way until every worker is a candidate, or k is reached
    stop = min(k, workers - (candidates * 2))
    while i < stop:
        if front[0] <= end[0]:
            total += front.pop(0)
            bisect.insort_right(front, costs.pop(0))
        else:
            total += end.pop(0)
            bisect.insort_right(end, costs.pop(-1))
        i += 1

    remaining = sorted(front + end)
    for j in range(k-i):
        total += remaining[j]

    return total



if __name__ == '__main__':
    testCosts = [31,25,72,79,74,65,84,91,18,59,27,9,81,33,17,58]
    testK = 11
    testCandidates = 2
    print(totalCost(testCosts, testK, testCandidates))


"""
Calculate how many workers will need to be hired before every worker is a
candidate.

Have two sorted lists of candidates, one for the candidates from the front of
the list and one from the end of the list.

For each iteration take whichever value is lower between the two lists. If
taking from the "front" list, grab the next candidate from the front of the
list. If taking from the "end" list, grab the next candidate from the end list.

Sort all the remaining candidates and add the lowest costs to the total until
all necessary workers have been hired.
"""