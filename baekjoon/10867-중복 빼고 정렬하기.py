N = int(input())
nums = list(map(int,input().split()))
nums = list(set(nums))
print(*sorted(nums))