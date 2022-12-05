import random


# Helper Functions
def switch_elements(i: int, j: int, n: list) -> list:
    n[i], n[j] = n[j], n[i]
    print('Tausche : ' + str(n[i]) + ' mit ' + str(n[j]))
    return n


def partition(A: list, p: int, r: int) -> int:
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A = switch_elements(i, j, A)
    A = switch_elements(i + 1, r, A)
    return i + 1


# Sorting Algorithms
def bubble_sort(n: list) -> list:
    n_len = len(n)
    for i in range(n_len - 1):
        for j in range(0, n_len - i - 1):
            print('Vergleich: ' + str(n[j]) + ' mit ' + str(n[j + 1]))
            if n[j] > n[j + 1]:
                n = switch_elements(j, j + 1, n)
    return n


def quick_sort(A: list, p: int, r: int) -> list:
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)
    return A


def rek_sort(A: list, start: int, end: int) -> list:
    m: int = start
    for i in range(start, end + 1):
        a = A[i]
        b = A[m]
        print('Vergleich: ' + str(a) + ' mit ' + str(b))
        if a > b:
            m = i
    if m != end:
        A = switch_elements(m, end, A)
    if end > start:
        A = rek_sort(A, start, end - 1)
    return A


def count_pair(n: list) -> list:
    pairs: dict = {}
    for i, element in enumerate(n):
        if element in pairs:
            pairs[element] += 1
        else:
            pairs[element] = 1

    pair_list = []
    for k, v in pairs.items():
        pair_list.append((k, v))
    return pair_list


if __name__ == "__main__":
    # Aufgabe 1 mit allen Ausgaben für a) und b)
    aufgabe_1_liste = [2, 5, 3, 8, 4, 7]
    print('Aufgabe 1:')
    print(bubble_sort(aufgabe_1_liste))

    # Aufgabe 2 mit allen Ausgaben für a) und b)
    aufgabe_2_liste = [3, 18, 12, 9, 24, 6, 21, 15]
    print('Aufgabe 2:')
    print(quick_sort(aufgabe_2_liste, 0, len(aufgabe_2_liste) - 1))

    # Aufgabe 3 mit allen Ausgaben
    aufgabe_3_liste = [1, 3, 5, 4, 2]
    print('Aufgabe 3:')
    print(rek_sort(aufgabe_3_liste, 0, len(aufgabe_3_liste) - 1))

    # Aufgabe 4 mit allen Ausgaben
    aufgabe_4_liste = []
    for number in range(0, 100):
        aufgabe_4_liste.append(random.randint(1, 10))
    print(count_pair(aufgabe_4_liste))
