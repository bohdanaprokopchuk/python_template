import pandas as pd


def input_console():
    user_int_value = int(input("Please enter a random number between 5 and 20: "))
    return user_int_value


def read_from_file():
    with open('F:/python-for-big-data-and-data-science/file_to_read') as file:
        file_content = file.read()
    return file_content


def read_from_file__using_pandas():
    df = pd.read_csv('F:/python-for-big-data-and-data-science/file_to_read')
    file_content_2 = df.to_string()
    return file_content_2
