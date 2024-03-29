from typing import Dict

FILEPATH = 'filepath'

BYTES = 'bytes'
LINES = 'lines'
WORDS = 'words'
CHARS = 'chars'

FLAGS: Dict[str, str] = {
    BYTES: '-c',
    LINES: '-l',
    WORDS: '-w',
    CHARS: '-m',
}

FLAGS_HELP: Dict[str, str] = {
    BYTES: 'outputs the number of bytes in a file',
    LINES: 'outputs the number of lines in a file',
    WORDS: 'outputs the number of words in a file',
    CHARS: 'outputs the number of characters in a file',
}
