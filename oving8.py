from sys import stdin
import math


def min_coins_greedy(coins, value, money):
    print('greedy: ')
    temp = 0
    for coin in coins:
        if value > coin:
            temp = math.floor(value / coin)
            value = value % coin
            money += temp
    return money


def min_coins_dynamic(coins, value):
    print('dynamic')
    temp = 0
    money = 0
    for coin in coins:
        if value > coin:
            temp = math.floor(value / coin)
            value = value % coin
            money += temp
    return money


def can_use_greedy(coins, value, money):
    greedy = True
    for i in range(len(coins)-1):
        if coins[i] % coins[i+1] != 0:
            greedy = False
            break
    if greedy:
        return min_coins_greedy(coins, value, money)
    else:
        return min_coins_dynamic(coins, value)

coins = []
for c in stdin.readline().split():
    coins.append(int(c))
coins.sort()
coins.reverse()
method = stdin.readline().strip()
if method == "dynamisk":
    for line in stdin:
        money = 0
        print(min_coins_dynamic(coins, int(line)))
else:
    if method == "graadig":
        for line in stdin:
            money = 0
            print(min_coins_greedy(coins, int(line), money))
    else:
        for line in stdin:
            money = 0
            print(can_use_greedy(coins, int(line), money))