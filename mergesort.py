def mergeSort(aList):
    if len(aList) > 1:
	mid = len(aList) / 2

	left = aList[mid:]
	right = aList[:mid]

	mergeSort(left)
	mergeSort(right)

	i, j, k = 0, 0, 0
	while(i < len(left) and j < len(right)):
	    if left[i] < right[j]:
    		aList[k] = left[i]
    		i+=1
	    else:
    		aList[k] = right[j]
    		j+=1
	    k+=1

	while(i < len(left)):
	    aList[k] = left[i]
	    i+=1
	    k+=1

	while(j < len(right)):
	    aList[k] = right[j]
	    j+=1
	    k+=1

aList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(aList)
print(aList)
