s = input()
ele = ['MON','TUE','WED','THU','FRI','SAT', 'SUN']

index = [i for i in range(7) if ele[i] == s][0]
ans = 6 -index
if ans == 0:
    print(7)
else:
    print(ans)
