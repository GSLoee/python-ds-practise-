def vowel_count(phrase):
    vowels = 'aeiou'
    count_dict = {}
    for vowel in phrase:
        if vowel == vowels in count_dict:
            count_dict[vowel] += 1
        else: 
            count_dict[vowel] = 1
    return count_dict   
    
    if count_dict
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """