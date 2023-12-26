fichero_entrada = "diadedivulgacion.in"
lista_salida = []

t = []

with open(fichero_entrada, "rt") as f:
    temp = f.readline()
    n = int(temp)
    for i in range(n):
        temp = f.readline().strip().split(" ")
        # iorig, start, duration, cant
        iorig, start, duration, cant = i, *(int(c) for c in temp)
        mi_fila = [cant, iorig, start, duration]
        t.append(mi_fila)

ts = sorted(t, reverse=False)


for fila in ts:
    print(fila)
print(t)