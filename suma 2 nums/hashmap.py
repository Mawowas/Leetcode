
nums = [10, 1, 5, 3, 7]

target = 8

diccionario = {}
lista_respuestas = []

for i, cada_numero in enumerate(nums):
    complemento = target - cada_numero

    if complemento in diccionario.keys():
        lista_respuestas.append(diccionario.get(complemento))
        lista_respuestas.append(i)
    else:
        diccionario[cada_numero] = i

print(lista_respuestas)
