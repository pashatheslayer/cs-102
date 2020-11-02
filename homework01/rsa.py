import random
import typing as tp
from math import sqrt


def is_prime(n: int) -> bool:
    """
    Tests to see if a number is prime.
    >>> is_prime(2)
    True
    >>> is_prime(11)
    True
    >>> is_prime(8)
    False
    """
    if n != 1:
        for i in range(2, round(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    return False


def gcd(a: int, b: int) -> int:
    """
    Euclid's algorithm for determining the greatest common divisor.
    >>> gcd(12, 15)
    3
    >>> gcd(3, 7)
    1
    """
    if b != 0:
        while a % b != 0:
            a, b = b, a % b
        return b
    else:
        return a


def multiplicative_inverse(e: int, phi: int) -> int:
    """
    Euclid's extended algorithm for finding the multiplicative
    inverse of two numbers.
    >>> multiplicative_inverse(7, 40)
    23
    """
    d = 1
    while d * e % phi != 1:
        d += 1
    return d


def generate_keypair(p: int, q: int) -> tp.Tuple[tp.Tuple[int, int], tp.Tuple[int, int]]:
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    elif p == q:
        raise ValueError("p and q cannot be equal")

    n = p*q

    phi = (p-1)*(q-1)

   
    e = random.randrange(1, phi)

    
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    
    d = multiplicative_inverse(e, phi)

    
    return ((e, n), (d, n))


def encrypt(pk: tp.Tuple[int, int], plaintext: str) -> tp.List[int]:
    
    key, n = pk
    
    
    cipher = [(ord(char) ** key) % n for char in plaintext]
    
    return cipher


def decrypt(pk: tp.Tuple[int, int], ciphertext: tp.List[int]) -> str:
    
    key, n = pk
    
    plain = [chr((char ** key) % n) for char in ciphertext]
    
    return "".join(plain)

print(is_prime(1))