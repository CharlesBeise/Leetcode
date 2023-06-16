def addDigits(num):
    while num > 9:
        numStr = str(num)
        num = 0
        for i in range(len(numStr)):
            num += int(numStr[i])

    return num


if __name__ == '__main__':
    myNum = 38
    print(addDigits(myNum))
