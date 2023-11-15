def single_letter_count(word, letter):
    total = 0
    for char in word.lower():
        if char == letter:
            total +=1
    return total
        
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """