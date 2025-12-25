"""
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""


def añadir_dos_numeros(lista1, lista2):

    # numero1 = ""
    # numero2 = ""

    # for cada_numero_lista1 in range(len(lista1)):
    #     numero1 += str(lista1[cada_numero_lista1])

    # for cada_numero_lista2 in range(len(lista2)):
    #     numero2 += str(lista2[cada_numero_lista2])
    # suma = int(numero1) + int(numero2)
    # lista = []
    # suma_cadena = str(suma)

    # for i in suma_cadena:
    #     lista.insert(0, i)

    # return lista

    suma_total = 0
    suma1 = 0
    suma2 = 0
    lista = []

    for i in lista1:
        
        suma_total += i 

        if (i >= 10):
            resto = (i ) % 10
            cociente = (i ) // 10

    return suma_total


def main():

    l1 = [9, 9, 9, 9, 9, 9, 9]
    l2 = [9, 9, 9, 9]

#    print(añadir_dos_numeros(l1, l2))

    print(38 // 10)
    print(28 % 10)


if __name__ == '__main__':
    main()
