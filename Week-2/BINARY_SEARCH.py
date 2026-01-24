'''Question- Given a sorted array of positive integers containing few duplicate 
             elements, design an algorithm and implement it using a program to find 
             whether the given key element is present in the array or not. 
             If present, then also find the number of copies of given key. (Time Complexity = O(log n))'''



def first_occurrence(arr, n, key):
    low = 0
    high = n - 1
    result = -1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == key:
            result = mid
            high = mid - 1      # move left
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return result


def last_occurrence(arr, n, key):
    low = 0
    high = n - 1
    result = -1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == key:
            result = mid
            low = mid + 1       # move right
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return result



T = int(input("Enter number of test cases: "))

while T > 0:
    n = int(input("Enter size of the array: "))
    print("Enter the sorted array elements (space separated):")
    arr = list(map(int, input().split()))

    key = int(input("Enter the key element: "))

    first = first_occurrence(arr, n, key)

    if first == -1:
        print("Key not present")
    else:
        last = last_occurrence(arr, n, key)
        count = last - first + 1
        print(f"{key}-{count}")

    T -= 1