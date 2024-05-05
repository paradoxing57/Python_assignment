def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid  # Return the index of the target if found
        elif arr[mid] < target:
            left = mid + 1  # Update the left pointer
        else:
            right = mid - 1  # Update the right pointer

    return -1  # Return -1 if the target is not found

# Example usage
arr = [1, 2, 3, 5, 7, 9, 10]
target = 7
result = binary_search(arr, target)

if result != -1:
    print(f"Target {target} found at index {result}.")
else:
    print(f"Target {target} not found in the array.")
