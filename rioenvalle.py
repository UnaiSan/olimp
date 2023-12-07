from typing import List, Tuple

def get_extreme(matrix: List[List[int]], max_: bool=True) -> Tuple[int, int, int]:
    if max_:
        func = max
    else:
        func = min
    extremes = []
    jextremes = []
    for f in matrix:
        extreme = func(f)
        jextreme = f.index(extreme)
        extremes.append(extreme)
        jextremes.append(jextreme)
    value = func(extremes)
    ivalue = extremes.index(value)
    jvalue = jextremes[ivalue]

    return value, ivalue, jvalue


def get_max(matrix: List[List[int]]) -> Tuple[int, int, int]:
    maxis = []
    jmaxis = []
    for f in matrix:
        maxi = max(f)
        jmaxi = f.index(maxi)
        maxis.append(maxi)
        jmaxis.append(jmaxi)
    top = max(maxis)
    itop = maxis.index(top)
    jtop = jmaxis[itop]

    return top, itop, jtop

def get_min(matrix: List[List[int]]) -> Tuple[int, int, int]:
    minis = []
    jminis = []
    for f in matrix:
        mini = min(f)
        jmini = f.index(mini)
        minis.append(mini)
        jminis.append(jmini)
    bot = min(minis)
    ibot = minis.index(bot)
    jbot = jminis[ibot]

    return bot, ibot, jbot



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

# maxis = []
# imaxis = []
# for fila in t:
#     maxi = max(fila)
#     maxis.append(maxi)
#     imaxis.append(fila.index(maxi))

# top = max(maxis)
# itop = maxis.index(top)
# jtop = imaxis[itop]

top, itop, jtop = get_max(t)

t_peque = [f[jtop-1:jtop+2] for f in t[itop-1:itop+2]]
bot, ibot, jbot = get_min(t_peque)

while 

print(f"{top = }, at i, j = {itop}, {jtop}")
print(f"check: {t[itop][jtop] = }")

print(f"{t_peque = }")

print(f"{bot = }, at i, j = {ibot}, {jbot}")