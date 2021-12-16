a, b = map(int, input().split())
nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,13, 1]
a_index = [i for i in range(len(nums)) if nums[i] == a][0]
b_index = [i for i in range(len(nums)) if nums[i] == b][0]

if b_index > a_index:
    print("Bob")
elif b_index < a_index:
    print("Alice")
else:
    print("Draw")
