def rotate_array(arr, n):
    if not isinstance(arr, list):
        raise ValueError("Input must be an array")
    
    if not isinstance(n, int):
        raise ValueError("n must be an integer")
    
    n = n % len(arr)
    return arr[-n:] + arr[:-n]

print(rotate_array([1, 2, 3, 4, 5], 2))
print(rotate_array([1, 2, 3, 4, 5], -1))
print(rotate_array("not a list", 2))