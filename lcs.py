def lcs(str1, str2):
    return lcs_helper(str1, str2, {})

def lcs_helper(str1, str2, memo):
    if str1 == "" or str2 == "":
        return 0
    else:
        if not(str1 in memo and str2 in memo[str1]):
            if str1 not in memo:
                memo[str1] = {}
            if str2 not in memo[str1]:
                memo[str1][str2] = 0
            if str1[len(str1)-1] == str2[len(str2)-1]:
                memo[str1][str2] = 1 + lcs_helper(str1[:len(str1)-1], str2[:len(str2)-1], memo)
            else:
                memo[str1][str2] = max(lcs_helper(str1[:len(str1)-1],str2,memo),
                                        lcs_helper(str1,str2[:len(str2)-1],memo))
        return memo[str1][str2]

print lcs("ABCDGH", "AEDFHR")
print lcs("AGGTAB", "GXTXAYB")
print lcs("AXYT", "AYZX")
