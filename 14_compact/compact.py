def compact(lst):
    remove = ['', [], False, (), None]
    
    return [item for item in lst if item not in remove]
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """