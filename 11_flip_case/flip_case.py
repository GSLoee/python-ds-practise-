def flip_case(phrase, to_swap):
    str = ''
    for letter in phrase:
        if letter != to_swap.lower():
            str += letter.lower()
        else:
            str += letter.upper()
    return str

            

    
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
