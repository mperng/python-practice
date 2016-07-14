def triple_step(n):
    if n > 2:
        prev = [2, 1, 1]
        for i in xrange(3,n+1):
            prev.insert(0, prev[0] + prev[1] + prev[2])
            prev.pop()
        return prev[0]
    else:
        if n < 3:
            return n
        elif n == 3:
            return 4
        else:
            return -1 # throw some error


print triple_step(0)
print triple_step(1)
print triple_step(2)
print triple_step(3)
print triple_step(4)
print triple_step(5)
print triple_step(35)
