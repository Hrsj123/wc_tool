import locale

def num_of_bytes(text: str) -> str:
    """Returns the total bytes present in file """
    res = 0
    for char in text:
        res += len(char.encode('utf-8'))
    return str(res)

def num_of_lines(text: str) -> str:
    """Returns the total number of lines used in a file"""
    return str(len(text.split('\n')))

def num_of_words(text: str) -> str:
    """Returns the total number of words used in a file"""
    return str(len(text.split(' ')))

def num_of_characters(text: str) -> str:
    """Returns the number of characters in a file"""
    encoding = 'windows-1252' if locale.getlocale()[1] == '1252' else 'utf-8'
    try:
        res = 0
        for char in text:
            res += len(char.encode(encoding))
    except UnicodeEncodeError:     
        res = num_of_bytes(text)
    return str(res)
