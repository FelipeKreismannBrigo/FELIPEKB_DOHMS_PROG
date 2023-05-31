#Objetivo: Criar um programa que printe os numeros de uma lista e, depois, eles multiplicados por 2
#Bonus: Colocar os numeros multiplicados em uma outra lista e printa-la

lista = [2, 3, 7, 12, 2]
lista_multiplicada = []

print("Números da lista original:")
for numero in lista:
    print(numero)

for numero in lista:
    numero_multiplicado = numero * 2
    lista_multiplicada.append(numero_multiplicado)

print("Números multiplicados por 2:")
for numero in lista_multiplicada:
    print(numero)
