nomes = ["Felipe", "Ricardo", "Lavínia", "Valentina", "Pedro"]

nomes_ordenados = sorted(nomes)

print("Nomes em ordem alfabética:")
for nome in nomes_ordenados:
    print(nome)

nomes_ordenados_ultima_letra = sorted(nomes, key=lambda x: x[-1])

print("Nomes em ordem alfabética da última letra:")
for nome in nomes_ordenados_ultima_letra:
    print(nome)