# --- DESAFÍO FINAL UNIDAD 3: COLECCIONES ---
# Objetivo: Limpiar y manipular la lista sin tocar la original.

lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]
print(f"1. Original: {lista}")

# 1. Borrar duplicados
# Paso a set (borra repes) y vuelvo a list.
# A partir de aca laburo con 'lista_nueva' para no romper la original.
lista_nueva = list(set(lista))
print(f"2. Sin duplicados: {lista_nueva}")

# 2. Ordenar mayor a menor
lista_nueva.sort(reverse=True)
print(f"3. Ordenada des: {lista_nueva}")

# 3. Eliminar impares
# OJO ACA: Itero sobre una COPIA ([:]) porque si borro elementos
# de la lista real mientras la recorro, se corren los indices y falla.
for n in lista_nueva[:]:
    if n % 2 != 0:  # Si el resto es distinto de 0, es impar
        lista_nueva.remove(n)

print(f"4. Solo pares: {lista_nueva}")

# 4. Sumar todo lo que quedo
suma_total = sum(lista_nueva)
print(f"5. Suma total: {suma_total}")

# 5. Insertar la suma al principio (indice 0)
lista_nueva.insert(0, suma_total)
print(f"6. Final con suma agregada: {lista_nueva}")

# 6. Check final
# El primer elemento (suma_total) tiene que ser igual a la suma del resto.
# Uso Slicing [1:] para sumar desde el segundo hasta el final.
verificacion = lista_nueva[0] == sum(lista_nueva[1:])

print(f"\n--- VALIDACION ---")
print(f"Dan los numeros: {verificacion}")  # Tiene que dar True
