# Challenge 78 - 2 fiddy
# Created: 17/09/2026
# Last Updated: 17/09/2026

def count_coin_combinations(target, coins):
    dp = [0] * (target + 1)
    dp[0] = 1  # Base case: There is 1 way to make 0p (using no coins)

    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] += dp[i - coin]

    return dp[target]

denom = [200, 100, 50, 20, 10, 5, 2, 1]

total_ways = count_coin_combinations(250, denom)
print(f"Total unique ways to make £2.50: {total_ways}")

'''
def find_coin_combinations(target, coins):
    def backtrack(remaining, start_index, current_combination, file_handle):
        if remaining == 0:
            file_handle.write(str(current_combination) + "\n")
            print(current_combination)
            return
        
        for i in range(start_index, len(coins)):
            coin = coins[i]
            if coin <= remaining:
                backtrack(remaining - coin, i, current_combination + [coin], file_handle)

    with open("ccombinations.txt", "w", encoding="utf-8") as file:
        backtrack(target, 0, [], file)

denom = [5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

find_coin_combinations(250, denom)
'''
