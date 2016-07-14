# return the index where the target is found; else return -1
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) / 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# why does mid need to be incremented or decremented? I am guessing
# that it is because each iteration of the search is reducing
# the search space to only the range that the target may be found in.
# In the case of mid != target, we know for sure mid does not contain
# target and want to exclude it from the reduced search space (whether we
# are going higher or lower)

print binary_search([1,3,5,8,9,11,15,20,30], 40)
print binary_search([1,3,5,8,9,11,15,20,30], 0)
print binary_search([1,3,5,8,9,11,15,20,30], 9)
print binary_search([1,3,5,8,9,11,15,20,30], 30)
print binary_search([1,3,5,8,9,11,15,20,30], 1)
print binary_search([1,3,5,8,9,11,15,20,30], 3)
print binary_search([1,3,5,8,9,11,15,20,30], 4)
