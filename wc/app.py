import os
from sys import stdin
from .function import num_of_bytes, num_of_lines, num_of_words, num_of_characters
from .reader import read_file
from .constants import FLAGS, FILEPATH
from .utils import arg_parser

def main() -> None:
    args = arg_parser()

    # Identify the flags
    flags = [FLAGS[flag] for flag in FLAGS.keys() if flag in set(args.keys())]
    if not flags:
        flags = FLAGS.values()

    # Check the file input-path / file-content (stdin)
    file_path = args[FILEPATH]
    is_file_valid = file_path and os.path.exists(file_path)
    content_bytes = read_file(file_path) if is_file_valid else stdin.buffer.read()

    # Calculate the result
    result = []
    for flag in flags:
        if flag == FLAGS['bytes']:
            output = num_of_bytes(content_bytes)
        elif flag == FLAGS['lines']:
            output = num_of_lines(content_bytes)
        elif flag == FLAGS['words']:
            output = num_of_words(content_bytes)
        elif flag == FLAGS['chars']:
            output = num_of_characters(content_bytes)
        result.append(output)

    print(f"   {'   '.join(result)}   {file_path if is_file_valid else '::stdin'}")