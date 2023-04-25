import re

def __init__(string):
    # Define the regular expression pattern
    pattern = r'nyetak\("(.+)"\)'

    # Define the replacement string
    replacement = r'print(\1)'

    # Use the sub() method to perform the replacement
    new_string = re.sub(pattern, replacement, string)

    # Output the new string
    return new_string
