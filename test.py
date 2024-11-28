def rotate_array(arr, n):
    if not isinstance(arr, list):
        raise ValueError("Input must be an array")
    
    if len(arr) == 0:
        return arr
    
    if not isinstance(n, int):
        raise ValueError("n must be an integer")
    
    n = n % len(arr)
    return arr[-n:] + arr[:-n]

print(rotate_array([], 2))