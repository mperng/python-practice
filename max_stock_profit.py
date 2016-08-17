"""
Algorithm:
Discover local maxima in the prices list. Iterate through the list and pop
off of the local maxima list if current index exceeds last local maximum index.
Keep a calculation of maximum profit using the current min price and local
maximum at the top of the local_maxima list.

Performance:
Algorithm runs in O(N) time and takes O(N) space. Since the stock market opens
at 9:30am and closes at 4pm, the space taken by the local_maxima list does not
exceed 390 in size (assuming the prices list is minute-by-minute as shown in
the example).
"""
def maxStockProfit(prices=[]):
    # return list of tuples of index, value for local maximum values in the
    # prices list
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

def isLocalMax(index, value, prices):
    if index == 0:
        return value > prices[index + 1]
    elif index == len(prices) - 1:
        return value > prices[index - 1]
    else:
        return value > prices[index - 1] and value > prices[index + 1]
