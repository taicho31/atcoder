# b
n = int(input())

p500 = n // 500
remain = n % 500

p5 = remain // 5
remain %= 5

print(p500 * 1000 + p5 * 5)
