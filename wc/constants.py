from typing import List

FLAGS: dict[str: str] = {
    'bytes': '-c',
    'lines': '-l',
    'words': '-w',
    'chars': '-m',
}

# Only considering the flags which can be calculated by utf-8 encoding!
DEFAULT_FLAG_KEYS: List[str] = [
    'bytes',
    'lines',
    'words',
]