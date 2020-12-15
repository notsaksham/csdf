#!/bin/python3

import random
import string
import sympy as spy


def keygen(type, size):
    if type == "printable":
        return """""".join(random.sample(list(string.printable), size))
    # if type == "numbers":
    #    return """""".join(random.sample(list(string.digits), size))
    # if type == "letters":
    #    return """""".join(random.sample(list(string.ascii_letters), size))
    # if type == "oct":
    #    return """""".join(random.sample(list(string.octdigits), size))
    # if type == "hex":
    #    return """""".join(random.sample(list(string.hexdigits), size))


def list_primes(n):
    primes = []
    for i in range(1, n+1):
        primes.append(spy.ntheory.generate.prime(i))
    return primes


def generate_final_key():
    key0 = keygen("printable", len(string.printable))
    key1 = keygen("printable", len(string.printable))
    return key0 + key1


def main():

    print("s-box key = ", keygen("printable", 100))
    range = int(input("till where? "))
    print("list of primes upto len(message) = ", list_primes(range))
    print("primes = e", (list_primes(10)))


if __name__ == '__main__':
    main()
