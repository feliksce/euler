# Largest prime factor
# Problem 3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

from math import floor, sqrt


def prime_test(number):
    if number == 1: return False
    if number == 2: return True
    if number == 3: return True

    # trial division method
    low = 2
    high = int(floor(number**0.5))

    for each in range(low, high+1, 1):
        if not number % each == 0: continue
        else: return False
    return True

lst = []

for number in range(1, 600851475143):
    if prime_test(number): lst.append(number)
print(lst[-1])
