# b
n, k =map(int, input().split())
def base10int(value, base):
    if (int(value / base)):
        return base10int(int(value / base), base) + str(value % base)
    return str(value % base)

num = base10int(n,k)
print(len(str(num)))
