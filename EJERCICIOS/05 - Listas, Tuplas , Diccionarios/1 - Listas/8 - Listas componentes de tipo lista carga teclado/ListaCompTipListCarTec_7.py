# Desarrollar un programa que cree una lista de 50 elementos. El primer elemento es una lista
# con un elemento entero, el segundo elemento es una lista de dos elementos etc.
# La lista debería tener esta estructura y asignarle esos valores a medida que se crean los elementos:
# [[1], [1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5], etc....]

# 1. Definimos la lista principal vacía
lista = []

# 2. Bucle externo para crear los 50 elementos (sublistas)
# Usamos range(1, 51) para que el primer valor sea 1 y el último 50
for k in range(1, 51):
    sublista = []
    # 3. Bucle interno para llenar la sublista actual
    # Agrega números desde 1 hasta el valor actual de k
    for x in range(1, k + 1):
        sublista.append(x)
    
    # 4. Añadimos la sublista terminada a la lista principal
    lista.append(sublista)

# 5. Imprimimos la lista resultante
print("Lista de 50 elementos con estructura creciente:")
print(lista)

# Verificación opcional del último elemento
print(f"\nCantidad de sublistas: {len(lista)}")
print(f"El último elemento contiene {len(lista[-1])} números.")