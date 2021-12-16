nums = list(map(int, input().split()))
maxi = max(nums)
remain = sum(nums) - maxi

if maxi == remain:
    print("Yes")
else:
    print("No")
