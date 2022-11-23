def maxProfit(prices):
    counter = 0
    for i in range(1, len(prices)):
        if prices[i] - prices[i - 1] > 0:
            counter += (prices[i] - prices[i - 1])
    return counter

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([1,2,3,4,5]))