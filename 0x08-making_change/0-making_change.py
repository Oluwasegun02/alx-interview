#!/usr/bin/python3

def makeChange(coins, total):

    if total <= 0:
        return 0
    process_total = [float('inf')] * (total + 1)
    process_total[0] = 0

    for coin in coins:
        for value in range(coin, total + 1):
            process_total[value] = min(process_total[value], process_total[value - coin] + 1)

        if process_total[total] == float('inf'):
            return - 1
    return process_total[total]

