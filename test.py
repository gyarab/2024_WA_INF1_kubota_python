def vowels_and_consonants(text):
    if not isinstance(text, str):
        raise ValueError('Input must be a string')

    vowels = 0
    consonants = 0
    for char in text:
        if char.lower() in 'aeěiíoóuůú':
            vowels += 1
        elif char.lower() in 'bcčdďfghjklmnpqrřsštťvwxzž':
            consonants += 1
    return {'vowels': vowels, 'consonants': consonants}