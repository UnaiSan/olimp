fichero_entrada = "haar.out"
lista_salida = []

t = []

with open(fichero_entrada, "rt") as f:
    temp = f.readline().strip().split(" ")
    vec_in = list(map(float, temp))
    n = len(vec_in)

vec_out = [x for x in vec_in]
n_last = n

while n_last >= 2:
    for i in range(n_last//2):
        a, b = vec_in[2*i : 2*i+2]
        m = (a + b) / 2
        d = a - m
        vec_out[i] = m
        vec_out[i + n_last//2] = d
    vec_in = [x for x in vec_out]
    n_last = n_last//2

print(f"last {vec_out = }")

print(f"{n = }, {vec_in = }")
print(f"{vec_out = }")