from sys import stdin
import math


def min_coins_greedy(coins, value, money):
    temp = 0
    for coin in coins:
        if value >= coin:
            temp = math.floor(value / coin)
            value = value % coin
            money += temp
    return money


def dynamic(coins, value):
    m = min_coins_dynamic(coins, value)
    for c in range(1, len(coins) + 1):
        for r in range(1, value + 1):
            if coins[c - 1] == r:
                m[c][r] = 1
            elif coins[c - 1] > r:
                m[c][r] = m[c - 1][r]
            else:
                m[c][r] = min(m[c - 1][r], 1 + m[c][r - coins[c - 1]])
    return m[-1][-1]

# Lager en matrise
def min_coins_dynamic(coins, value):
    m = [[0 for _ in range(value + 1)] for _ in range(len(coins) + 1)]
    for i in range(value + 1):
        m[0][i] = i
    return m


def can_use_greedy(coins, value, money):
    greedy1 = True
    for i in range(len(coins)-1):
        if coins[i] % coins[i+1] != 0:
            greedy1 = False
            break
    if greedy1:
        return min_coins_greedy(coins, value, money)
    else:
        fromGreedy = 0
        temp = 0
        x = len(coins) - 1
        for i in range(len(coins) - 1):
            if value >= coins[i]:
                if coins[i] % coins[i+1] == 0:
                    temp = math.floor(value / coins[i])
                    value = value % coins[i]
                    fromGreedy += temp
                    x -= 1
                else:
                    return (dynamic(coins, value) + fromGreedy)
        return (dynamic(coins, value) + fromGreedy)

coins = []
for c in stdin.readline().split():
    coins.append(int(c))
coins.sort()
coins.reverse()
method = stdin.readline().strip()
if method == "graadig":
    for line in stdin:
        money = 0
        print(min_coins_greedy(coins, int(line), money))
elif method == "dynamisk":
    for line in stdin:
        print(dynamic(coins, int(line)))
else:
    for line in stdin:
        money = 0
        print(can_use_greedy(coins, int(line), money))