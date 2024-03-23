import argparse
import os
from sys import stdin
from .function import num_of_bytes, num_of_lines, num_of_words, num_of_characters
from .reader import read_file
from .constants import FLAGS, FLAGS_HELP, FILEPATH

def parser() -> dict:
    parser = argparse.ArgumentParser(
        prog='ccwc',
        description='A command-line utility inspired from Unix-based operating systems.',
        epilog='-------------------------- END --------------------------'
    )

    parser.add_argument(FILEPATH, help='The filepath where the file exists', nargs='?')
    for flag in FLAGS:
        parser.add_argument(
            FLAGS[flag], 
            f'--{flag}', 
            action='store_true',
            help=FLAGS_HELP[flag], 
        )

    args = parser.parse_args()
    return {key: value for key, value in vars(args).items() if value is not None or key == FILEPATH}

def main() -> None:
    args = parser()
    # Identify the flags
    if flags:
        flags = [FLAGS[flag] for flag in FLAGS.keys() if flag in set(args.keys())]
        if not flags:
            flags = FLAGS.values()

    # Check the file input-path / file-content (stdin)
    file_path = args[FILEPATH]
    is_file_valid = file_path and os.path.exists(file_path)
    content = read_file(file_path) if is_file_valid else stdin.read()

    # Calculate the result
    result = []
    for flag in flags:
        if flag == FLAGS['bytes']:
            output = num_of_bytes(content)
        elif flag == FLAGS['lines']:
            output = num_of_lines(content)
        elif flag == FLAGS['words']:
            output = num_of_words(content)
        elif flag == FLAGS['chars']:
            output = num_of_characters(content)
        result.append(output)

    print(f"   {'   '.join(result)}   {file_path if is_file_valid else '::stdin'}")