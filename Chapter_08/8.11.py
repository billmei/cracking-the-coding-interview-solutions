# Given an infinite number of quarters, dimes, nickles, and pennies,
# calculate the number of ways of representing n cents.

# Assume that n is an integer (can't have fractional cents)

# Is output an integer (the number of ways), or an array (showing the actual coins you would need?)
# I think the output should be an integer, this is like the knapsack problem

# for 0 ≤ n ≤ 4, there is only 1 way to make change.

# Are the coin types fixed or should we support the ability to add more coin types?
# First, assume it is fixed, then later add the ability to support more coins.


# NOTE! The solution in the book doesn't actually work because it's double-counting
# the same way to make coins.
# For example, the book says:
# makeChange(100 using 0 quarters) +
# makeChange(75 using 0 quarters) +
# makeChange(50 using 0 quarters) +
# makeChange(25 using 0 quarters) +
# + 1
# But this is wrong, because if you recursed into making change for 75 with 0 quarters,
# the next sub-recursive call would be making change with an extra quarter for 50 cents,
# but we cannot do this because we already accounted for this extra quarter
# in the previous step where we make change for 50 (so we are already using 2 quarters)
# A possible way to solve this is in the memoization function, allow returning
# from it only once (Does this work for pennies?), so that subsequent calls don't get counted
# The insight in the book is to pass the array with the denominations into the
# recursive call.


coins = [25, 10, 5, 1]

def num_ways_change(cents, memo={}):
    if cents < 0:
        raise ValueError("input must be >= 0")

    total_ways = 0
    if cents in memo:
        return memo.get(cents)

    for coin in coins:
        # Making change for 10 cents: 5 nickles and 5 pennies is the same as
        # 5 pennies and 5 nickles, so we have to make sure not to double
        # count this case.
        if cents < coin:
            continue
        if cents == coin:
            total_ways += 1 + num_ways_change(cents - 1, memo)
            # print(f"{coin} goes into {cents} exactly, and the total ways is {total_ways}")
            break
        else: # cents > coin
            num_coins = cents // coin
            leftover = cents - num_coins * coin
            # print(f"{coin} goes into {cents} {num_coins} times and {leftover} is leftover")
            real_leftover = 0
            if leftover > 4:
                real_leftover = num_ways_change(leftover, memo)
            total_ways += num_ways_change(coin, memo) + real_leftover
            break

    memo[cents] = total_ways
    # print(memo)
    return total_ways

print("num ways for 0:", num_ways_change(0))
print("num ways for 4:", num_ways_change(4))
print("num ways for 5:", num_ways_change(5))
print("num ways for 6:", num_ways_change(6))
print("num ways for 9:", num_ways_change(9))
print("num ways for 10:", num_ways_change(10))
print("num ways for 11:", num_ways_change(11))
print("num ways for 24:", num_ways_change(24))
print("num ways for 25:", num_ways_change(25))
print("num ways for 26:", num_ways_change(26))
print("num ways for 30:", num_ways_change(30))
print("num ways for 99:", num_ways_change(99))
print("num ways for 100:", num_ways_change(100))
print("num ways for 101:", num_ways_change(101))
print("num ways for 105:", num_ways_change(105))
# print("num ways for 99999999:", num_ways_change(99999999))