'''Question- Given a sorted array of positive integers, design an algorithm and implement it using a program to find three indices
             i, j, k such that arrli] + arr[j] = arr[k].
             def find_three_indices(arr, n): for k in range(n - 1, 1, -1):'''


def find_three_indices(arr, n):
    
    for k in range(n - 1, 1, -1):
        i = 0
        j = k - 1

        # Two-pointer approach
        while i < j:
            s = arr[i] + arr[j]

            if s == arr[k]:
                return True, i, j, k
            elif s < arr[k]:
                i += 1
            else:
                j -= 1

    return False, -1, -1, -1



T = int(input("Enter number of test cases: "))

while T > 0:
    n = int(input("Enter size of the array: "))
    print("Enter the sorted array elements (space separated):")
    arr = list(map(int, input().split()))

    found, iPos, jPos, kPos = find_three_indices(arr, n)

    if found:
        print("Indices found:", iPos, jPos, kPos)
    else:
        print("No sequence found")

    T -= 1

print("End of Program")