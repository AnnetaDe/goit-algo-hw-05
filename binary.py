def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    mid = 0
    counter = 0
    if arr[right] < x:
        return -1
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        return (arr[0], counter) if arr[0] == x else -1

    while left <= right:
        mid = (left + right) // 2
        counter += 1
        if arr[mid] == x:

            return (arr[mid + 1], counter)
        else:
            if arr[mid] < x:
                left = mid + 1
            elif arr[mid] > x:
                right = mid - 1
    return -1


print(binary_search([1.2, 2.3, 3.4, 4.6, 4.8, 5.5, 6.5, 7.8, 8.9, 9.1], 4.6))
print(binary_search([1.2, 2.3, 3.4, 4.6, 4.8, 5.5, 6.5, 7.8, 8.9, 9.1], 4.7))
print(binary_search([1.2], 1.2))
print(binary_search([1.2], 1.3))
print(binary_search([1.2, 2.3], 1.2))
