minhaLista = ["abacaxi", "melancia", "abacate"]
minhaLista2 = [1, 2, 3, 4, 5]
minhaLista3 = ["abacaxi", 2, 9.89, True]

tamanho = len(minhaLista3)
print(tamanho)

minhaLista.append("limão")

for item in minhaLista:
	print(item)

if 7 in minhaLista2:
	print("7 está na lista")
elif(3 in minhaLista2):
	print("3 está na lista")
else:
	print("Número não está na lista")

# Ordenar a lista
lista = [124,56,778,3,8,0,53,1654]
lista.sort()

print(lista)

#inverter (reverter) a lista
lista.reverse()
print(lista)