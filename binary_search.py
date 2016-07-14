# return the index where the target is found; else return -1
def binarySearch(sorted_list, target):
    if len(sorted_list) > 1:
        head, tail = 0, len(sorted_list)
        mid = (head - tail) / 2
        while head >= 0 and tail < len(sorted_list):
            if sorted_list[mid] == target:
                return True
            elif sorted_list[mid] < target:
                head = mid
                mid += (tail - head) / 2
            else: # sorted_list[mid] > target:
                tail = mid
                mid -= (mid - head) / 2
        return False
    else:
        if len(sorted_list) == 1 and sorted_list[0] != target:
            return True
        else
            return False
