#!/bin/python3


import math
import random
import string


def encrypt(message, key_length):
    rows = math.ceil(len(message) / key_length)

    matrix = [[] for x in range(rows)]

    for i in range(rows):
        matrix[i].append(message[i * key_length:(i + 1) * key_length])

    for i in range(key_length * rows - len(message)):
        matrix[-1][0] += str(random.choice(string.printable))

    cipher_matrix = [[] for x in range(key_length)]

    for i in range(key_length):
        for j in range(rows):
            cipher_matrix[i].append(matrix[j][0][i])

    cipher_text = ""
    for i in range(key_length):
        cipher_text += "".join(cipher_matrix[i])

    return cipher_text


def padding(message, key_length):
    return math.ceil(len(message) / key_length) * key_length - len(message)


def decrypt(message, key_length, pad):
    rows = math.ceil(len(message) / key_length)

    matrix = [[] for x in range(key_length)]

    for i in range(key_length):
        matrix[i].append(message[i * rows: (i + 1) * rows])

    plain_matrix = []
    for j in range(rows):
        for i in range(key_length):
            plain_matrix.append(matrix[i][0][j])

    for i in range(pad):
        plain_matrix.pop()

    return """""".join(plain_matrix)


def main():
    #message = "hellow how do you do? I am doing fine, thank you. What about you? I am also doing fine."
    print('input = ', message)

    key_length = 4
    cipher_text = encrypt(message, key_length)
    print("cipher text = ", cipher_text)

    pad = padding(message, key_length)
    original_text = decrypt(cipher_text, key_length, pad)
    print(original_text)


if __name__ == '__main__':
    main()
