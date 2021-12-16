s = int(input())

nums = [s]
count = 1
prev = s
while True:
    count += 1
    if prev % 2 == 0:
        new = prev //2
    else:
        new = 3 * prev + 1
    
    if new in nums:
        break
    nums.append(new)
    prev= new
print(count)
