def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def primes_in_range(a, b):
    if not isinstance(a, int) or not isinstance(b, int) or (a < 0) or (b < 0) or (b < a):
        raise ValueError("Error")
    primes = []
    for i in range(a, b+1):
        if is_prime(i):
            primes.append(i)
    return primes