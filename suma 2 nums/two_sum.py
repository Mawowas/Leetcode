# class Solution(object):
#     def twoSum(self, nums, target):
"""
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
nums = [3, 3]
respuesta = list()
print(nums)


def sumar_2_numeros(lista):
    i = 0
    j = 0
    target = 6

    for i, valor_i in enumerate(lista):
        for j, valor_j in enumerate(lista):
            if ((valor_j + valor_i) == target) and (i != j):
                respuesta.append(i)
                respuesta.append(j)
                return respuesta


def usando_hash_map():
    diccionario = {}
    lista_numeros = [2, 7, 11, 15]
    target = 9
    lista_respuesta = []

    # print("\nUsando HashMap\n")
    # for cont, cada_numero in enumerate(lista_numeros):
    #     complemento = target - cada_numero
    #     if complemento in diccionario:
    #         lista_respuesta.append(diccionario.keys)
    #     else:
    #         diccionario[cont] = cada_numero
    #     complemento = 0

    complemento = 0
    for i, cada_numero in enumerate(lista_numeros):

        complemento = target - cada_numero

        if complemento in diccionario.keys():
            lista_respuesta.append(diccionario.get(complemento))
            lista_respuesta.append(i)
        else:
            diccionario[cada_numero] = i

    return lista_respuesta


print("respuesta: ", sumar_2_numeros(nums))
print("Respuesta usando HashMap: ", usando_hash_map())

