from sys import argv, stdin
from .assertion_functions import check_file, check_flags
from .function import num_of_bytes, num_of_lines, num_of_words, num_of_characters
from .reader import read_file
from .constants import FLAGS, DEFAULT_FLAG_KEYS

def main() -> None:
    # Identify the flags
    if argv[1:]:
        flags = list(filter(lambda cli_input: cli_input.startswith('-'), argv[1:]))
        are_flags_valid, invalid_flags_list = check_flags(flags)
        if not are_flags_valid:
            raise ValueError(f"Invalid flags {' '.join(invalid_flags_list)} provided!")
        if not flags:
            flags = [FLAGS[key] for key in DEFAULT_FLAG_KEYS]

    # Check the file input-path / file-content (stdin)
    file_path = argv[-1]
    is_file_valid = check_file(file_path)
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