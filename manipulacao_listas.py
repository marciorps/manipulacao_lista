valores = [1,2,3,4,5, 2, 6,7,8,9,10]
anos = [2020, 2030, 2040, 2050]
#Adicionar ao final da lista
valores.append(11)
print(valores)
#unir listas(ela não retorna valor para criar uma nova lista)
# valores.extend(anos)
# print(valores)
#Adicionar lista(essa sim adiciona e pode ser colocada em uma nova variavel)
nova_lista = valores + anos
print(nova_lista)
#inserir um novo valor a lista
print(anos[1])
anos.insert(2, 2031)
print(anos)
#Estrair mas não modifica a lista com base no indice(e o valor com o pop pode ser rertonado)
anos_2020 = anos.pop(0)
print(anos_2020)
#Remover(por valor e não indice) item da lista(não o indice mais sim o valor)
# anos.remove(2050)
# print(anos)


del anos[3]#na função DEL pode ser excluido uma faixa de valores[2:6]
print(anos)

#Contando a ocorrencia de valores em uma lista
print(valores.count(2))

#Resetar ou excluir todos os itens dentro de uma lista
valores.clear()
print(valores)

