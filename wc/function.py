# import locale

def num_of_bytes(text: bytes) -> str:
    """Returns the total bytes present in file"""
    return str(len(text))

def num_of_lines(text: bytes) -> str:
    """Returns the total number of lines used in a file"""
    count = 0
    for line in text.decode('utf-8').split('\n'):
        count += 1 if line else 0
    return str(count)

def num_of_words(text: bytes) -> bytes:
    """Returns the total number of words used in a file"""
    count = 0
    for line in text.decode('utf-8').split('\n'):
        count += len(line.split())
    return str(count)

def num_of_characters(text: bytes) -> str:
    """Returns the number of characters in a file"""
    # encoding = 'windows-1252' if locale.getlocale()[1] == '1252' else 'utf-8'
    try:
        res = len(text.decode('utf-8'))

        ## Below code for locale based approach,
        ## Python implicitly handles multibyte characters!

        # res = 0
        # for char in text.decode(encoding):
        #     res += len(char)
    except UnicodeDecodeError:     
        res = num_of_bytes(text)
    return str(res)
