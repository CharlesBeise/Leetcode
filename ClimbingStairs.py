def climbStairs(n):
    if n == 1 or n == 2:
        return n

    first = 1
    second = 2

    for i in range(n - 2):
        result = first + second
        first = second
        second = result

    return result


if __name__ == '__main__':
    print(climbStairs(4))


"""
This is just a fibonacci sequence, because each time you add a step the result
is the sum of how many ways you can climb 1 fewer steps plus 1 step and how
many ways you can climb 2 fewer steps plus 2 steps.
"""