# Determine if a string has all unique characters

# Idea 1: Use a hashmap to track the characters used so far.
# This is O(n), but requires an additional data structure
def is_unique(chars):
    seen = {}
    for char in chars:
        if seen.get(char):
            return False

        seen[char] = 1

    return True

# Idea 2: Make a bit mask for each character, and check there is no overlap
# This is O(n), does not require an additional data structure, but
# this isn't memory efficient if you have a large alphabet, e.g. unicode
import string
alphabet = list(string.printable)
def is_unique(chars):
    vec = [0] * len(alphabet) # length of alphabet
    for char in chars:
        idx = alphabet.index(char)
        if vec[idx]:
            return False
        vec[idx] = 1
    return True

# Idea 3: Sort the string, and then make sure every character is different from the previous one
# But this takes O(n log n) time, compared to O(n) time.
def is_unique(chars):
    last_char = ""
    for char in sorted(chars):
        if char == last_char:
            return False

        last_char = char
    return True

assert is_unique("abc")
assert not is_unique("abcb")
assert is_unique("")
assert is_unique(" ")
print("All tests passed")

# Missed:
# - Assume a fixed alphabet. If the string is longer than this alphabet (e.g. 256),
# then we automatically know there must be a duplicated character via the pigeonhole principle,
# so we can return False right away.
# - Don't construct the bit vector explicitly, instead use a single int and
# |= and << bit shifts to check for duplicates.