n, nums= input(), map(int, input().split())
print(any(str(j) == str(j)[::-1] for j in nums) and all(i > 0 for i in nums))