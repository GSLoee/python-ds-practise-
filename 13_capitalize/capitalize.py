def capitalize(phrase):
    for cap in phrase:
        return phrase[0].upper() + phrase[1:]
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """