def split_into_threes(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    return [text[i:i+3] for i in range(0, len(text), 3)]