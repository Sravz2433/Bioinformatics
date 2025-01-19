def DPChange(money, Coins):
    MinNumCoins = [float('inf')] * (money + 1)
    MinNumCoins[0] = 0
    
    for m in range(1, money + 1):
        for coin in Coins:
            if m >= coin:
                if MinNumCoins[m - coin] + 1 < MinNumCoins[m]:
                    MinNumCoins[m] = MinNumCoins[m - coin] + 1
    
    return MinNumCoins[money]

# Example usage:
money = 16100
Coins = [17, 13, 5, 3, 1]
print(DPChange(money, Coins))  # Output: 3 (for coins [5, 5, 1])