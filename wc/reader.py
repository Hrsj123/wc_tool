def read_file(path: str, read_byte: bool=True, encoding: str='utf-8') -> str:
    kwargs = {
        'file': path,
        'mode': 'rb' if read_byte else 'r'
    }
    if not read_byte:
        kwargs.update(encoding=encoding)

    with open(**kwargs) as f:
        return f.read()