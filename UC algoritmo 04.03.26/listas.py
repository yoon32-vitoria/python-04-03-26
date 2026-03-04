nomes = ["Ana", "Bruno", "Caio"]#dados tipo string
print(nomes)

dados = ["Carol", 0, 1.70, True]#todos os tipos de dados, dado booleano(verdadeiro ou falso)
print(dados)
print(type(dados))
print(type(dados[0]))
print(type(dados[1]))
print(type(dados[2]))
print(type(dados[3]))

lista = ["Cachorro", "Gato"]
print("Original: ", lista)
lista.append("Coelho")#adicionar no final da lista(append)
print("Atualizado: ", lista)

lista.insert(1, "Grilo")#adicionar na posição determinada(insert)
print("Atualizado", lista)

lista.extend(["Macaco", "Ovelha"])#Adicionar mais de um dado de uma vez
print("Lista final", lista)