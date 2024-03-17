

def square_the_number(c):
    """
    Prints the value of c squared to the console.

    Args:
       c: The value to print

    Returns:
       The value of c squared.

    Raises:
       TypeError: invalid data type.
    """
    try:
        if c % 10 == 0:
            return c ** 2
        return None
    except TypeError:
        print("Invalid data type.")


def the_list_of_lines(filename, lines):
    """
       Writes the provided list of lines to a specified file.

       Args:
           filename (str): The name of the file to write to.
           lines (list): A list of strings, where each string represents a line to be written to the file.

       Raises:
           FileNotFoundError: If the specified file cannot be opened for writing.
       """
    try:
        with open(filename, 'w') as file2:
            file2.writelines(lines)
            print("File written successfully.")
    except FileNotFoundError:
        print(f"Error: File is not found.")
        return None
