import argparse
from .constants import FILEPATH, FLAGS, FLAGS_HELP

def arg_parser() -> dict:
    DESCRIPTION = 'A command-line utility inspired from Unix-based operating systems to get information about text file.'
    EPILOG = f'{"-" *(len(DESCRIPTION) // 2 - 2)} END {"-" *(len(DESCRIPTION) // 2 - 2)}'

    parser = argparse.ArgumentParser(
        prog='ccwc',
        description=DESCRIPTION,
        epilog=EPILOG,
    )

    parser.add_argument(FILEPATH, help='The filepath where the file exists', nargs='?')

    for flag in FLAGS.keys():
        parser.add_argument(
            FLAGS[flag], 
            f'--{flag}', 
            action='store_true',
            help=FLAGS_HELP[flag], 
        )

    args = parser.parse_args()
    return {key: value for key, value in vars(args).items() if value is not None or key == FILEPATH}