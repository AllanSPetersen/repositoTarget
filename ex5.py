# entrada da string
string = input("Digite a string a ser invertida: ")

# converter string em lista
lista = list(string)

# inverter a lista
for i in range(len(lista)//2):
    lista[i], lista[len(lista)-i-1] = lista[len(lista)-i-1], lista[i]

# converter lista de volta para string
string_invertida = ''.join(lista)

# imprimir string invertida
print("A string invertida é:", string_invertida)