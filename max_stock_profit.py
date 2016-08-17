def isLocalMax(index, value, prices):
    if index == 0:
        return value > prices[index + 1]
    elif index == len(prices) - 1:
        return value > prices[index - 1]
    else:
        return value > prices[index - 1] and value > prices[index + 1]

def maxStockProfit(prices=[]):
    local_maxima = filter(lambda x : isLocalMax(x[0], x[1], prices),
                          enumerate(prices))
    if not prices or not local_maxima:
        return 0
    minPrice = prices[0]
    maxProfit = local_maxima[0][1] - minPrice
    for index, value in enumerate(prices):
        if index > local_maxima[0][0]:
            local_maxima.pop(0)
            if not local_maxima:
                break
        minPrice = min(minPrice, value)
        maxProfit = max(maxProfit, local_maxima[0][1]-minPrice)
    return maxProfit
