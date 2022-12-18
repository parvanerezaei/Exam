def minSwaps(arr):
    swaps = 0
    n = len(arr)

    for idx in range(n):
        while arr[idx] - 1 != idx:
            ele = arr[idx]
            arr[ele - 1], arr[idx] = arr[idx], arr[ele - 1]
            swaps += 1
    print(swaps)

#minimumSwaps([7,1,3,2,4,5,6])

