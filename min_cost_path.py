def min_cost_path(cost, m, n):
    memo = [[None for i in xrange(len(cost[0]))] for j in xrange(len(cost))]
    return min_cost_path_helper(cost,m,n,0,0,memo)

def min_cost_path_helper(cost, m, n, i, j, memo):
    if i == m and j == n:
        return cost[i][j]
    if not memo[i][j]:
        if i + 1 <= m and j + 1 <= n:
            memo[i][j] = cost[i][j] + min(min_cost_path_helper(cost,m,n,i+1,j,memo),
                                          min_cost_path_helper(cost,m,n,i,j+1,memo),
                                          min_cost_path_helper(cost,m,n,i+1,j+1,memo))
        elif i + 1 <= m:
            memo[i][j] = cost[i][j] + min_cost_path_helper(cost,m,n,i+1,j,memo)
        else:
            memo[i][j] = cost[i][j] + min_cost_path_helper(cost,m,n,i,j+1,memo)
    return memo[i][j]

print min_cost_path([[1,2,3],[4,8,2],[1,5,3]],2,2)
print min_cost_path([[1,2,3],[2,2,2],[1,5,3]],2,2)
