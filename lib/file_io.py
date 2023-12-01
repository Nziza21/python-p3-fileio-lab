# lib/file_io.py

def write_file(file_name, file_content):
    """
    Writes the given content to a text file with the specified name.

    Args:
    - file_name (str): The name of the file (including the extension).
    - file_content (str): The content to be written to the file.
    """
    with open(f'{file_name}.txt', 'w') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    """
    Appends the given content to a text file with the specified name.

    Args:
    - file_name (str): The name of the file (including the extension).
    - append_content (str): The content to be appended to the file.
    """
    with open(f'{file_name}.txt', 'a') as file:
        file.write(append_content)

def read_file(file_name):
    """
    Reads the content of a text file with the specified name.

    Args:
    - file_name (str): The name of the file (including the extension).

    Returns:
    - str: The content of the file.
    """
    with open(f'{file_name}.txt', 'r') as file:
        return file.read()