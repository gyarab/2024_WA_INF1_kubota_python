def is_prime(number):
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Input must be an integer")
    else:
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

print(is_prime(2))
print(is_prime(10))
print(is_prime(13))