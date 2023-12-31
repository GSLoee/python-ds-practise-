def frequency(lst, search_term):
    total = 0
    for list in lst: 
        if list == search_term:
            total += 1
    return total

    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """
print(frequency([1, 4, 3, 4, 4], 4))