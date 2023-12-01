n = int(input())

colores = 0

res = 1
for i in range(n):
    b = input().split(" ")
    bb = [int(e) for e in b]
    print(bb[:i])
    for e in bb[:i]:
        res *= e
    colores += res

print(colores)