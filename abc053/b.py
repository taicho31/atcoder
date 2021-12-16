s = input()
a_pos = len(s.split("A")[0]) + 1
z_pos = len(s) - len(s.split("Z")[-1]) 
print(z_pos - a_pos + 1)
