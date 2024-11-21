def fibonacci(n):
    if isinstance(n, int):
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]
        else:
            fib_sequence = [0, 1]
            while len(fib_sequence) < n:
                next_number = fib_sequence[-1] + fib_sequence[-2]
                fib_sequence.append(next_number)
            return fib_sequence
    else:
        return ("invalid input")

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def fahrenheit_to_kelvin(fahrenheit):
    kelvin = (fahrenheit + 459.67) * 5/9
    return kelvin

def kelvin_to_fahrenheit(kelvin):
    fahrenheit = (kelvin * 9/5) - 459.67
    return fahrenheit

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius