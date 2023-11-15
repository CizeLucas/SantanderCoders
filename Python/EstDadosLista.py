notas = [7.9, 9.7, 8.2, 6.2, 4.7, 2.3]

## criar uma lista vazia: lista = []  ou  lista = list()

lista_de_lista = [notas, "PythonEhBrabo", True, 999]
##                  0      1           2           3     4 
##                  -5     -4          -3         -2     -1
print("O tamanho de lista_de_lista eh: "+str(len(lista_de_lista)))
print(f"{lista_de_lista[-3]} oh: {lista_de_lista}")
print(notas[2:4]) ##sleciona o conteudo dos indices [x,y] -> x ate (y-1)
print(notas[4:])
print(notas[::2]) ##imprime todos os elementos incrementando de 2 em 2
print("\n")
"""
for elemento in lista_de_lista: {
    print(elemento)
}
"""

for elemento in range(len(lista_de_lista)):
    print(lista_de_lista[elemento])

