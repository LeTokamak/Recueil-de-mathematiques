

liste_a_tester = [2,3,5,7,11,
13,17,19,23,29,
31,37,41,43,47,
53,59,61,67,71,
73,79,83,89,97]


def is_prime(n):
    """
    Test if a number is prime.

    :param n: Integer to test for primality
    :return: True if n is a prime number, False otherwise
    """
    # Handle edge cases
    if n <= 1:
        return False
    if n <= 3:
        return True

    # Check for even number
    if n % 2 == 0:
        return False

    # Only check for factors up to the square root of n
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True

for e in liste_a_tester :
    if is_prime(e):
        print(f"{e} est premier !")
    else :
        print(f"{e} N4EST PAS PREMIER")