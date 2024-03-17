import pandas as pd


def triples_the_number_from_console():
    """
    Prompts the user to enter an integer between 5 and 20, triples the entered number.

    Returns:
      Your number, but tripled or an error message if the user enters an invalid data type.

    Raises:
      TypeError: invalid data type.
    """

    try:
        user_int_value = int(input("Please enter a random number between 5 and 20: "))
        if 5 <= user_int_value <= 20:
            return f"Your number has been tripled: {user_int_value * 3}"
    except TypeError:
        print("Invalid input. Please enter a valid integer.")


def turns_to_characters(filename):
    """
    Reads the contents of a file with the given name,
    capitalizes each letter in a given string and returns these characters in different rows.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        Characters of the file content capitalized in different rows,
        or an error message if the file is not found or the content is not a string.

    Raises:
        FileNotFoundError: If the file is not found.
        TypeError: If the file content is not a string.
    """
    try:
        with open(filename, 'r') as file:
            file_content = file.read()
            if not isinstance(file_content, str):
                raise TypeError("Argument must be a string.")
            else:
                for i in range(0, len(file_content)):
                    print(file_content[i].upper())
                return "It works!"
    except FileNotFoundError:
        print(f"Error: File is not found.")


def show_name_rgb(filename):
    """
      Reads a CSV file using Pandas, extracts the "Name" and "RGB" columns,
      print only those columns.

      Args:
          filename (str): The name of the CSV file to read from.

      Returns:
          A Pandas DataFrame containing only the "Name" and "RGB" columns from the file,
          or None if the file is not found.

      Raises:
          FileNotFoundError: If the specified file is not found.
      """
    try:
        df = pd.read_csv(filename)
        df = df[["Name", "RGB"]]
        print(df.to_string())
        return df
    except FileNotFoundError:
        print(f"Error: File is not found.")
        return None
