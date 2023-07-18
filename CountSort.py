def countSort(arr):
    minVal = min(arr)
    rangeVal = max(arr) - minVal + 1

    count = [0] * rangeVal

    for num in arr:
        count[num - minVal] += 1

    for i in range(1, rangeVal):
        count[i] += count[i - 1]

    sorted_arr = [0] * len(arr)

    for num in reversed(arr):
        sorted_arr[count[num - minVal] - 1] = num
        count[num - minVal] -= 1

    return sorted_arr


if __name__ == "__main__":
    A = list(map(int, input().strip('[').strip(']').split(',')))

    print(countSort(A))
