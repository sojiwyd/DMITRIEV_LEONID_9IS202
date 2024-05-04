map = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
print(map)

def binarySearch(map):
    easy = 0
    hard = len(map) - 1

    while easy <= hard:
        mid = (easy + hard) // 2
        if map[mid] == 1 and map[mid-1] == 0:
            return mid
        elif map[mid] == 0:
            easy = mid + 1
        else:
            hard = mid - 1

    return -1

result = binarySearch(map)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")