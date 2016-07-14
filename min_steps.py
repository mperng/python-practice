def min_steps(n):
    assert(n >= 1)
    return min_steps_helper(n, 0, [0, 1, 1, 2] + ([None] * n))

def min_steps_helper(n, num_steps, prev):
    if prev[n-1]:
        return num_steps + prev[n-1]
    else:
        if n % 3 == 0:
	    print "dividing by 3: " + str(n/3)
	    prev[n-1] = min_steps_helper(n / 3, num_steps + 1, prev)
	elif n % 2 == 0:
	    print "dividing by 2: " + str(n/2)
	    prev[n-1] = min_steps_helper(n / 2, num_steps + 1, prev)
	else:
	    print "sub 1: " + str(n-1)
	    prev[n-1] = min_steps_helper(n - 1, num_steps + 1, prev)
	print "storing in prev: " + str.format("{} : {}", n, prev[n-1])
	return prev[n-1]

print min_steps(7)
print min_steps(16)
print min_steps(50)
