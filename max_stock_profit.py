def isLocalMax(index, value, prices):
    return (index == 0 and value > prices[index+1]) or \
       (index == len(prices) - 1 and value > prices[index - 1]) or \
       (index > 0 and index < len(prices) - 1 and value > prices[index - 1]
        and value > prices[index+1])

def maxStockProfit(prices):
    if not prices:
        return 0
    local_maxima = filter(lambda x : isLocalMax(x[0], x[1], prices),
                          enumerate(prices))
    i, minPrice, maxProfit = 1, prices[0], local_maxima[0][1]-prices[0]
    for i in xrange(1, len(prices)):
        if i > local_maxima[0][0]:
            local_maxima.pop(0)
            if not local_maxima:
                break
        minPrice = min(minPrice, prices[i])
        maxProfit = max(maxProfit, local_maxima[0][1]-minPrice)
    return maxProfit
