# Diving board
# laying planks end ot end
# 2 types: "shorter", "longer"
# Use exactly K planks of wood

# Assumptions

# NOTE: it doesn't say this in the book, but we are actually returning
# the integer number of combinations, not the exact combinations.

# Don't know the exactly length
# the two lengths are coprime.
# Given an input k, generate all possible lengths

# Examples
# 2 planks

# shorter, shorter
# longer, shorter
# shorter, longer
# longer, longer

# input: 2, output: [
# (shorter, shorter)
# (longer, shorter)
# (shorter, longer)
# (longer, longer)
#]

# Algo

# O(2^n) if not memoized (every step, we double the number of ops)
# O(1) space if not memoized
# O(n) if memoized
# O(n^2) space if memoized, plus O(n) for the call stack (the list is O(n) long, and each element contains O(n) objects, and it's triangular, so O((1/2) n^2)).

# Code
def plank_lengths(num_planks):
  if num_planks < 0:
    print("Can't have negative planks")
    return

  memo = {}
  memo[0] = []
  memo[1] = [["short"], ["long"]]
  lengths = range(num_planks)

  # Make it iterative instead of recursive to avoid running out of call
  # stack space.
  for length in lengths:
    _plank_lengths(length, memo)

  return _plank_lengths(num_planks, memo)

def _plank_lengths(num_planks, memo={}):
  if memo.get(num_planks) is not None:
    return memo.get(num_planks)
  print("_plank_lengths", num_planks)

  previous_combos = []

  memoized_result = memo.get(num_planks-1)
  if memoized_result is not None:
    previous_combos = memoized_result
  else:
    print("This should never happen")
    # previous_combos = _plank_lengths(num_planks-1, memo)

  all_combos = []

  # Recurse, for num_planks-1, add a short, and also a long
  for combo in previous_combos:
    combo1 = combo.copy()
    combo2 = combo.copy()
    combo1.append("short")
    combo2.append("long")
    all_combos.append(combo1)
    all_combos.append(combo2)

  memo[num_planks] = all_combos
  return all_combos

# Test
# print(plank_lengths(1))
# print(plank_lengths(2))
# print(plank_lengths(3))
# print(plank_lengths(90))


# Alternate solution: Just go through all unique sets:

def plank_lengths(num_lengths):
  lengths = []
  for i in range(num_lengths+1):
    lengths.append((["short"] * i) + (["long"] * (num_lengths-i)))
  return lengths

# Or itertools:

import itertools
def plank_lengths(num_lengths):
  return list(itertools.combinations_with_replacement(["short", "long"], num_lengths))

print(plank_lengths(1))
print(plank_lengths(2))
print(plank_lengths(3))
