fichero_entrada = "supermercado.in"

d_prods = {}
with open(fichero_entrada, "rt") as f:
    n_kilos_coger = int(f.readline())
    n_productos = int(f.readline())
    for i in range(n_productos):
        p, d = f.readline().strip().split(" ")
        d_prods[i] = int(p), int(d)

print(f"{d_prods = }")