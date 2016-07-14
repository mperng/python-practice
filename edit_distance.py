def edit_distance(str1, str2):
    memo = [[ -1 for i in xrange(len(str2)) ] for j in xrange(len(str1))]
    return edit_distance_helper(str1,str2,len(str1)-1, len(str2)-1, memo)

def edit_distance_helper(str1, str2, m, n, memo):
    if m < 0 or n < 0:
        return 0 if m == n else (max(m,n) + 1)
    if memo[m][n] == -1:
        if str1[m] == str2[n]:
            memo[m][n] = edit_distance_helper(str1, str2, m-1, n-1, memo)
        else:
            memo[m][n] = 1 + min(edit_distance_helper(str1,str2,m,n-1,memo),
                                 edit_distance_helper(str1,str2,m-1,n,memo),
                                 edit_distance_helper(str1,str2,m-1,n-1,memo))
    return memo[m][n]

print edit_distance("gesek", "geek")
print edit_distance("cut", "cat")
print edit_distance("saturday", "sunday")
