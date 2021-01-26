# The Masseuse: A popular masseuse receives a sequence of back-to-back
# appointment requests, and we need to schedule the highest total booked
# minutes that can be booked. Return the number of minutes.
# The masseuse needs a 15-min break between appointments.


a = [30, 15, 60, 75, 45, 15, 15, 45]
# a = [1, 1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 6, 7, 8, 8, 8 ]
output = 180


# Skip 1
# Skip 2

# Take the first open appointment
# Skip

# Take the next open appointment
# Recurse

# Backtrack: Skip 2
# Take the next
# REcurse

# Backtrack: Skip 3,
# etc.


# Memoize backtracked results,
# Save a starting point, 

# O(2^n) without memoization
# O(n^2) with memoization

# a = [15, 60, 15]

def appointment_minutes(appts = [], memo = {}):
    backtrack_depth = []

    if memo.get(str(appts)) is not None:
        return memo.get(str(appts))

    most_time_so_far = 0
    for i in range(len(appts)):
        time = appts[i]
        try:
            time += appointment_minutes(appts[i+2:], memo)
        except IndexError:
            pass
        most_time_so_far = max(most_time_so_far, time)

    memo[str(appts)] = most_time_so_far
    return most_time_so_far

print()
print(appointment_minutes(a))
