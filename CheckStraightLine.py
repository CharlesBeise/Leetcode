def checkStraightLine(coordinates):
    pointA = coordinates[0]
    pointB = coordinates[1]

    try:
        slope = (pointB[1] - pointA[1]) / (pointB[0] - pointA[0])
    except ZeroDivisionError:
        if pointB[0] - pointA[0] == 0:
            for point in coordinates:
                if point[0] != pointA[0]:
                    return False
            return True
        else:
            for point in coordinates:
                if point[1] != pointA[1]:
                    return False
            return True

    for i in range(2, len(coordinates)):
        pointA = coordinates[i - 1]
        pointB = coordinates[i]

        try:
            curSlope = (pointB[1] - pointA[1]) / (pointB[0] - pointA[0])
        except ZeroDivisionError:
            return False

        if curSlope != slope:
            return False

    return True


if __name__ == '__main__':
    testCoordinates = [[0,0],[0,1],[0,-1]]
    print(checkStraightLine(testCoordinates))
