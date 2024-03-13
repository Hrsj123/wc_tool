def read_file(path: str, read_byte: bool=False) -> str:
    kwargs = {
        'file': path,
        'mode': 'rb' if read_byte else 'r'
    }
    if not read_byte:
        kwargs.update(encoding='utf-8')

    with open(**kwargs) as f:
        return f.read()