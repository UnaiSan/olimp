fichero_entrada = "haar.in"
lista_salida = []

t = []

with open(fichero_entrada, "rt") as f:
    temp = f.readline()
    n = int(temp)
    temp = f.readline().strip().split(" ")
    vec_in = list(map(int, temp))


print(f"{n = }, {vec_in = }")