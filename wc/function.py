def num_of_bytes(text: str) -> str:
    """Returns the total bytes present in file 
        (1-char consumes 1-byte in utf-8 encoding)"""
    return str(len(text))

def num_of_lines(text: str) -> str:
    """Returns the total number of lines used in a file"""
    return str(len(text.split('\n')))

def num_of_words(text: str) -> str:
    """Returns the total number of words used in a file"""
    return str(len(text.split(' ')))

def num_of_characters(byte_input: bytes) -> str:
    """Returns the number of characters in a file"""
    # If the current locale does not support multibyte characters this will match the -c option
    ### NOT SURE OF THE LOGIC USED HERE!
    return str(len(byte_input))
