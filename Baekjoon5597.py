a = list(range(1, 31))

for _ in range(28):
    n = int(input())
    a.remove(n)

print(min(a))
print(max(a))