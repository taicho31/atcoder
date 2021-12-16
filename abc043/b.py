import collections

# [ input ]
keys = input()
 
queue = collections.deque()
for c in keys:
    if c in ["0", "1"]:
        queue.append(c)
    elif c == "B":
        if len(queue):
            queue.pop()
# output chars
output = ""
while len(queue):
    output += queue.popleft()
    
# [ output ]
print(output)
