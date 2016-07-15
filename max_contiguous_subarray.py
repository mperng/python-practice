# a recursive version I formulated on my own with a memo table.
# It broke with extremely large datasets
def mcs_recursive(arr):
    memo = [None] * len(arr)
    return mcs_helper(arr,1,arr[0],memo)

def mcs_helper(arr, i, sum, memo):
    if i == len(arr):
        return sum
    else:
        if not memo[i]:
            memo[i] = max(sum,
                          mcs_helper(arr,i+1,sum+arr[i], memo),
                          mcs_helper(arr,i+1,arr[i], memo))
        return memo[i]

# the version adapted from a wikipedia article
def mcs(arr):
    max_end_here = max_so_far = arr[0]
    for i in xrange(1, len(arr)):
        max_end_here = max(max_end_here + arr[i], arr[i])
        max_so_far = max(max_so_far, max_end_here)
    return max_so_far


def mncs(arr):
    result = arr[0]
    for i in xrange(1, len(arr)):
        if result < 0:
            result = max(result, result + arr[i], arr[i])
        else:
            result = result + arr[i] if arr[i] > 0 else result
    return result

print str(mcs([1,2,3,4])) + " " + str(mncs([1,2,3,4]))
print str(mcs([2, -1, 2, 3, 4, -5])) + " " + str(mncs([2,-1,2,3,4,-5]))
print str(mcs([-1, -2, -3, -4, -5])) + " " + str(mncs([-1,-2,-3,-4,-5]))
