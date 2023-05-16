def addBinary(a, b):
    binA = int(a, 2)
    binB = int(b, 2)

    val = binA + binB

    return str(bin(val))[2:]


if __name__ == '__main__':
    a = "11"
    b = "1"
    print(addBinary(a, b))
