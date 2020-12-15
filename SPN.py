#!/bin/python3

import sbox
import pbox
import keygen
import time


def encrypt(plain_text, key, prime, stage):
    print("plain text = ", plain_text)
    e_text_1 = pbox.encrypt(plain_text, prime)
    e_text_2 = sbox.substitute_encrypt(e_text_1, key)
    return e_text_2


def decrypt(plain_text, encrypted_text, key, prime, stage):
    d_text_2 = sbox.substitute_decrypt(encrypted_text, key)
    padding = pbox.padding(plain_text, prime)
    d_text_1 = pbox.decrypt(d_text_2, prime, padding)
    return d_text_1


def main():
    key_list = []
    key = keygen.generate_final_key()
    key_list.append(key[:100])
    key_list.append(key[100:])

    stages = int(input("how many stages? > "))
    for i in range(stages):
        key_list.append(sbox.substitute_encrypt(key_list[i+1], key_list[1]))

    total_start = time.time()
    primes = keygen.list_primes(stages)
    print("key = ", key)
    print("primes = ", primes)
    print("\n========================================\n")

    with open('test.txt', 'r') as file:
        plain_text = file.read()

    encrypted_text = []
    encrypted_text.append(plain_text)

    print("--- Encryption ---")
    for i in range(stages):
        start = time.time()
        encrypted_text.append(encrypt(encrypted_text[i], key_list[i+1], primes[i], i+1))
        end = time.time()
        print (f"\nTime taken for encryption in stage {i} is :{end-start}")
       #print(f"encrypted stage {i+1} text = ")

    print("\n========================================\n")

    decrypted_text = []
    decrypted_text.insert(0, encrypted_text[-1])
    print("--- Decryption ---")
    print("text to be decypted = ", decrypted_text[0])

    for i in range(stages, 0, -1):
        start = time.time()
        decrypted_text.insert(0, decrypt(encrypted_text[i-1], encrypted_text[i], key_list[i], primes[i-1], i))
        end = time.time()
        print (f"\nTime taken for decryption in stage {i} is :{end-start}")
        print(f"decrypted stage {i} text = ", decrypted_text[0])

    total_end = time.time()
    file1 = open('decryptedtext.txt','w')
    file1.write(decrypted_text[0])
    file1.close()

    print("\n\inTotal time taken is", total_end - total_start)


if __name__ == '__main__':
    main()
