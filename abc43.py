##### a
n = int(input())
print(n*(n+1)//2)

##### b
import collections 

keys = input() 

queue = collections.deque() 
for c in keys:
    if c in ["0", "1"]:
        queue.append(c)
    elif c == "B":
        if len(queue):
            queue.pop()

output = ""
while len(queue):
    output += queue.popleft()

print(output)
