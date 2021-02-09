def stockmax(prices):
    max_price = prices[len(prices)-1]
    profit = 0

    for i in range(len(prices)-1, -1, -1):
        if max_price < prices[i]:
            max_price = prices[i]
        profit += (max_price - prices[i])
    return profit
