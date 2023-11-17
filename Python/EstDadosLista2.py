
lista = [3, 4, 7, 9]
print(lista)

lista.append(0)
print(f"lista.append(0): {lista}")

lista.insert(1, 4)
lista.insert(len(lista), 5)
print(f"lista.insert(...): {lista}")

lista.pop()
print(f"lista.pop(): {lista}")

lista.pop(4)
print(f"lista.pop(2): {lista}")

lista.remove(7)
print(f"lista.remove(7): {lista}")

print(f"lista.count(4): {lista.count(4)}")

print(f"lista.index(4): {lista.index(4)}")

lista.sort()
print(f"Lista apos o .sort() {lista}")

lista.sort(reverse = True)
print(f"Lista apos o .sort() {lista}")

print(f"len(lista): {len(lista)}")

print(f"sum(lista): {sum(lista)}")

print(f"max(lista): {max(lista)}")

print(f"min(lista): {min(lista)}")