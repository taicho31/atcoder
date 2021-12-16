n = int(input())
cards = sorted(list(map(int, input().split())), reverse=True)

alice = sum(cards[0::2])
bob = sum(cards[1::2])

print(alice - bob)
