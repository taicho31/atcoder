import itertools
n = int(input())
nums = [i for i in range(1,n+1)]

ptr = list(itertools.permutations(nums, n))

a1 = tuple(map(int, input().split()))
a2 = tuple(map(int, input().split()))    
           
a1_index = [i for i in range(len(ptr)) if ptr[i]==a1][0]
a2_index = [i for i in range(len(ptr)) if ptr[i]==a2][0]

print(abs(a1_index - a2_index))
