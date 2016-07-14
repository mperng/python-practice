def can_sort(arr):
    for i in xrange(len(arr) - 2):
        if not (arr[i] < arr[i+1] < arr[i+2]):
            tries = 0
            while(not (arr[i] < arr[i+1] < arr[i+2]) and
                  tries < 2):
                rotate(arr, i, i+1, i+2)
                tries += 1
            print arr
            if tries >= 2 and not (arr[i] < arr[i+1] < arr[i+2]):
                return False
    return True        
                
def rotate(arr, a, b, c):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = arr[c]
    arr[c] = temp

def all_sorted(arr):
    i = 1
    while(i < len(arr)):
        if arr[i-1] > arr[i]:
            return False
    return True


num_test_cases = int(raw_input())
for test_case in xrange(num_test_cases):
    n = int(raw_input())
    a = map(int, str(raw_input()).split(" "))
    if(all_sorted(a)):
        print "YES"
    else:
        print "YES" if can_sort(a) else "NO"
