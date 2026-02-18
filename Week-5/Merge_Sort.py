''' Question:-  Implement Merge Sort in Python to sort an array of integers using the Divide and Conquer approach.'''


def merge(arr, left, mid, right):
    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]

    i = 0
    j = 0
    k = left

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)


# ---------------- Driver Code ----------------

if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    arr = list(map(int, input("Enter elements separated by space: ").split()))

    if len(arr) != n:
        print("Error: Number of elements entered does not match n.")
    else:
        print("Original Array:", arr)
        merge_sort(arr, 0, n - 1)
        print("Sorted Array:", arr)
