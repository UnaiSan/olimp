fichero_entrada = "haar.in"
lista_salida = []

t = []

with open(fichero_entrada, "rt") as f:
    temp = f.readline()
    n = int(temp)
    temp = f.readline().strip().split(" ")
    vec_in = list(map(float, temp))

vec_out = [x for x in vec_in]
vec_in = [x for x in vec_out]
n_last = 2

while n_last <= n:
    for i in range(n_last//2):
        m, d = vec_in[i], vec_in[i+n_last//2]
        a = d + m
        b = m - d
        vec_out[2*i] = a
        vec_out[2*i + 1] = b
    vec_in = [x for x in vec_out]
    n_last = n_last * 2


print(f"{n = }, {vec_in = }")
print(f"{vec_out = }")