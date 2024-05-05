def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target if found
    return -1  # Return -1 if the target is not found

# Example usage
arr = [3, 5, 1, 9, 2, 7]
target = 9
result = linear_search(arr, target)

if result != -1:
    print(f"Target {target} found at index {result}.")
else:
    print(f"Target {target} not found in the array.")
