# def main():
#     n = int(input())
#     prices = list(map(int, input().split()))

#     # Initialize minimum buying price with the first day's price
#     minPrices = prices[0]

#     # Initialize maximum profit as 0
#     maxProfit = 0

#     # Iterate through the prices starting from the second day
#     for i in range(1, len(prices)):
#         # Check if today's stock price is lower than the minimum price
#         # If yes, update the minimum buying price
#         if prices[i] <minPrices:
#             minPrices = prices[i]
#         # Calculate the profit if we sell the stock today
#             Profit = prices[i]-minPrices
#         # Check if the current profit is greater than maximum profit
#             if Profit > maxProfit:
#                 maxProfit = Profit
#         # If yes, update maximum profit
#     # Print the maximum profit
#     print(maxProfit)


# if __name__ == "__main__":
#     main() 





def main():
    n = int(input())
    prices = list(map(int, input().split()))

    minPrice = prices[0]
    maxProfit = 0

    for i in range(1, n):

        # Update minimum buying price
        if prices[i] < minPrice:
            minPrice = prices[i]

        # Calculate profit if we sell today
        currentProfit = prices[i] - minPrice

        # Update maximum profit
        if currentProfit > maxProfit:
            maxProfit = currentProfit

    print(maxProfit)


if __name__ == "__main__":
    main()
