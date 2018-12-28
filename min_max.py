numbers = [1, 2, '0', '300', -2.5, 'Dog', True, 0o1256, None]

sortedIntList = []

for item in numbers:
    if type(item) == int:
        sortedIntList.append(item)
    elif type(item) == float:
        sortedIntList.append(int(item))
    try:
        if item.isnumeric():
            sortedIntList.append(int(item))
    except:
        print("Type of item is " + str(type(item)))

    # elif type(item) == str and item.isnumeric():
    #         sortedIntList.append(int(item))

print(sortedIntList)

for i, item in enumerate(sortedIntList):
    print("Type of item with index {i} ".format(i=i) + " is " + str(type(item)))

maxValue = max(sortedIntList)
minValue = min(sortedIntList)

print("Max value is: " + str(maxValue))
print("Min value is: " + str(minValue))

