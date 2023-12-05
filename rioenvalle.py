fichero_entrada = "rioenvalle.in"

t = []

with open(fichero_entrada, "rt") as f:
    temp = f.readline().strip().split(" ")
    nf, nc = int(temp[0]), int(temp[1])
    for i in range(nf):
        temp = f.readline().strip().split(" ")
        t.append(temp)
        for j, v in enumerate(temp):
            t[i][j] = int(v)

maxis = []
imaxis = []
for fila in t:
    maxi = max(fila)
    maxis.append(maxi)
    imaxis.append(fila.index(maxi))

top = max(maxis)
itop = maxis.index(top)
jtop = imaxis[itop]


t_peque = []
ij_peque = [tuple(range(itop-1, itop+2)), tuple(range(jtop-1, jtop+2))]
for i, fila in enumerate(t[itop-1:itop+2]):
    t_peque.append(fila[jtop-1:jtop+2])

minis = []
iminis = []
for fila in t_peque:
    mini = min(fila)
    minis.append(mini)
    iminis.append(fila.index(mini))

bot = min(minis)
ibot = minis.index(mini)
jbot = ij_peque[1][ibot]

print(f"{maxis = }")
print(f"{imaxis = }")
print(f"{top = }, at i, j = {itop}, {jtop}")
print(f"check: {t[itop][jtop] = }")

print(f"{t_peque = }")
print(f"{ij_peque = }")

print(f"{minis = }")
print(f"{iminis = }")
print(f"{bot = }, at i, j = {ibot}, {jbot}")