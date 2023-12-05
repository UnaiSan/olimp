fichero_entrada = "supermercado.in"

productos = []  # (precio, cantidad, orden_original)
d_prods = {}
with open(fichero_entrada, "rt") as f:
    n_kilos_coger = int(f.readline())
    n_productos = int(f.readline())
    for i in range(n_productos):
        p, d = f.readline().strip().split(" ")
        productos.append((int(p), int(d), i))

productos_ordenados = sorted(productos)

mi_cesta = [0 for _ in range(n_productos)]
kilos_cogidos = 0
total = 0

while kilos_cogidos < n_kilos_coger:
    p, c, i = productos_ordenados.pop()
    me_quedan = n_kilos_coger - kilos_cogidos
    if c < me_quedan:
        kilos_cogidos += c
        mi_cesta[i] = c
        total += c * p
    else:
        kilos_cogidos += me_quedan
        mi_cesta[i] = me_quedan
        total += me_quedan * p

print(f"{n_kilos_coger = }")
print(f"{n_productos = }")
print(f"{productos = }")
print(f"{productos_ordenados = }")
print(f"{mi_cesta = }")

print(f"{kilos_cogidos = }")
print(f"{total = }")
for v in mi_cesta:
    print(v)
