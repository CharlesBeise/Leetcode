def minFlips(a, b, c):
    binA = str(bin(a))[2:]
    binB = str(bin(b))[2:]
    binC = str(bin(c))[2:]

    maxLen = max(len(binA), len(binB), len(binC))

    while len(binA) < maxLen:
        binA = '0' + binA

    while len(binB) < maxLen:
        binB = '0' + binB

    while len(binC) < maxLen:
        binC = '0' + binC

    flips = 0

    for i in range(len(binC)):
        if binC[i] == '0':
            flips = flips + int(binA[i]) + int(binB[i])
        elif binA[i] == '0' and binB[i] == '0':
            flips += 1

    return flips


if __name__ == '__main__':
    a = 5
    b = 2
    c = 8
    print(minFlips(a, b, c))
