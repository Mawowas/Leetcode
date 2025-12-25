"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros."""



"""arreglar el error de index"""
def main():
    l1 = [9,9,9,9,9,9,9]
    l2 = [9,9,9,9]

    #print(35 // 10,'\n', 35 % 10)

    print("\n",addTwoNumbers(l1, l2))


def addTwoNumbers(l1: list, l2: list) -> list:
    respuesta  = []

    #tam = min(len(l1), len(l2))
    tam = max(len(l1), len(l2))
    lmax = []
    lmin = []

    if len(l1) < len(l2):
        lmax = l2
        lmin = l1
    else:
        lmax = l1
        lmin = l2

    for n in range(tam):

        lmax[n] += lmin[n] 

        if lmax[n] >= 10:
            lmax[n + 1] += lmax[n] // 10
            lmax[n] = lmax[n] % 10
            respuesta.append(lmax[n])
        else:
            respuesta.append(lmax[n])
        print(f'{lmax[n]}', end=', ')

    return respuesta





if __name__ == "__main__":
    main()