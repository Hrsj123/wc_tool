import os
from typing import List
from .constants import FLAGS

def check_file(file_path: str) -> bool:
    """Check if the file at the file_path is present"""
    return os.path.exists(file_path)

def check_flags(flags: List[str]) -> tuple[bool, List[str]]:
    """Check if the flag present within flags are valid"""
    invalid_flags = []
    for flag in flags:
        if flag not in FLAGS.values():
            invalid_flags.append(flag)
    return len(invalid_flags) == 0, invalid_flags