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

def get_shape(matrix: List[List[int]]) -> Tuple[int, int]:
    return len(matrix), len(matrix[0])

fichero_entrada = "rioenvalle_2.in"
lista_salida = []

t = []

with open(fichero_entrada, "rt") as f:
    temp = f.readline().strip().split(" ")
    nf, nc = int(temp[0]), int(temp[1])
    for i in range(nf):
        temp = f.readline().strip().split(" ")
        t.append(temp)
        for j, v in enumerate(temp):
            t[i][j] = int(v)

top, itop, jtop = get_max(t)
lista_salida.append(top)

if (not itop in [0, nf-1]) or (not jtop in [0, nc-1]):
    t_peque = [f[jtop-1:jtop+2] for f in t[itop-1:itop+2]]
    t_peque[1][1] += 1000
    bot, ibot, jbot = get_min(t_peque)
    itop += ibot - 1
    jtop += jbot - 1
    lista_salida.append(bot)
    t[itop][jtop] += 1000

    while (not itop in [0, nf-1]) and (not jtop in [0, nc-1]):
        t_peque = [f[jtop-1:jtop+2] for f in t[itop-1:itop+2]]
        t_peque[1][1] += 1000
        bot, ibot, jbot = get_min(t_peque)
        itop += ibot - 1
        jtop += jbot - 1

        lista_salida.append(bot)        
        t[itop][jtop] += 1000

for s in lista_salida:
    print(s)