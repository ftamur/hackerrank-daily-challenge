from itertools import combinations_with_replacement

word, val = input().split()
combs = list(combinations_with_replacement(sorted(list(word)), int(val)))

[print("".join(comb)) for comb in combs]