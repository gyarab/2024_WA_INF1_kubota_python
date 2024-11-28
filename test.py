def rotate_array(arr, n):
    if not isinstance(arr, list):
        raise ValueError("Input must be an array")
    
    if not isinstance(n, int):
        raise ValueError("n must be an integer")
    
    n = n % len(arr)
    return arr[-n:] + arr[:-n]