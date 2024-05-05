def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        # Find the index of the smallest element in the remaining unsorted part
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the smallest element with the current element (at index i)
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Example usage
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)
