"""Ler uma lista de 10 números reais e
mostre-os na ordem inversa."""
lista_numero = []
for n in range(10):
    numero = float(input("Digite o seu numero:"))
    lista_numero.append(numero)
print(f"A lista normal ficou assim {lista_numero}")
print("Agora o inverso e ")
lista_numero.reverse()
