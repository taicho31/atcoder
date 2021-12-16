n = int(input())
nums = sorted(list(map(int, input().split())))

maxi = nums[-1]

if maxi < sum(nums) - maxi:
    print("Yes")
else:
    print("No")
