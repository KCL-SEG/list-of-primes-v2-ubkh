"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []

    if number_of_primes <= 0:
        raise ValueError("number_of_primes must be a positive integer")
    number = 2
    while len(list) < number_of_primes:
        is_prime = True
        for prime in list:
            if number % prime == 0:
                is_prime = False
                break
        if is_prime:
            list.append(number)
        number += 1
    return list
