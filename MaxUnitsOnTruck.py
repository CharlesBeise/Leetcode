def maximumUnits(box, trucksize):
    dict_box = {}
    for i in box:
        if i[1] in dict_box:
            dict_box[i[1]] += i[0]
        else:
            dict_box[i[1]] = i[0]
    sorted_dict_box = sorted(dict_box.items(), key=lambda x: x[0], reverse=True)

    boxes = 0
    check = 0
    units = 0

    print(sorted_dict_box)

    while boxes < trucksize:
        if len(sorted_dict_box) == 0:
            return units
        elif check < sorted_dict_box[0][1]:
            units += sorted_dict_box[0][0]
            check += 1
            if check == sorted_dict_box[0][1]:
                del sorted_dict_box[0]
                check = 0
        boxes += 1

    return units




if __name__ == '__main__':
    boxTypes = [[1,3],[5,5],[2,5],[4,2],[4,1],[3,1],[2,2],[1,3],[2,5],[3,2]]
    truckSize = 35

    print(maximumUnits(boxTypes, truckSize))
