

someList = [1, 2, '3', 4, 'name', 10, 33, 'Python']
sortedList = []


def filter_list(arr):
    for item in arr:
        if type(item) is int:
            sortedList.append(item)
        else:
            continue
    print(str(arr) + " == " + str(sortedList))


filter_list(someList)
