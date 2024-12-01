#!/usr/bin/python3
"""coins change"""


def makeChange(coins, total):
    """Determine the fewest number of coins needed"""
    if (total <= 0):
        return 0

    coins = sorted(coins, reverse=True)
    coin_count = 0

    for coin in coins:
        coin_count += total // coin
        total %= coin

        if (total == 0):
            return coin_count

    return -1
