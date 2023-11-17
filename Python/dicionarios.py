
dicionario = {"id": 0,"nome": "Walisson", "idade": 26, 'altura': 1.77}
print(dicionario)
print(dicionario["nome"])

dicionario["programador"]  = True
dicionario["idade"] = 27

print(dicionario)

for chave in dicionario:
    print(chave, dicionario[chave])

print("peso" in dicionario)
print("Altura" in dicionario)
print("altura" in dicionario)

"""
lista = [dicionario, {"id": 1,"nome": "Joao", "idade": 50, 'altura': 1.64}]
print(lista[1]["nome"])

for index in lista:
    for chave in index:
        print(chave, index[chave])
"""