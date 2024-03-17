from app.io.input import triples_the_number_from_console
from app.io.input import turns_to_characters
from app.io.input import show_name_rgb
from app.io.output import the_list_of_lines
from app.io.output import square_the_number


def main():
    with open("output_for_1.txt", "w") as output_file:
        print("Function 1: ")
        print("Function 1: ", file=output_file)
        text_from_console = triples_the_number_from_console()
        print(text_from_console)
        print(text_from_console, file=output_file)
        print("==" * 30)
        print("==" * 30, file=output_file)

        print("Function 2: ")
        print("Function 2: ", file=output_file)
        file_path1 = "./input.txt"
        text_from_file_python = turns_to_characters(file_path1)
        print(text_from_file_python)
        print(text_from_file_python, file=output_file)
        print("==" * 30)
        print("==" * 30, file=output_file)

        print("Function 3 (using pandas): ")
        print("Function 3 (using pandas): ", file=output_file)
        file_path2 = "./input_pandas.csv"
        text_from_file_pandas = show_name_rgb(file_path2)
        print(text_from_file_pandas)
        print(text_from_file_pandas, file=output_file)
        print("==" * 30)
        print("==" * 30, file=output_file)

    print("  ")
    print("Function 4 (to console): ")
    text_to_console = square_the_number(5000)
    print(text_to_console)
    print("=="*30)

    print("Function 5 (to file): ")
    file_path3 = "./output.txt"
    lines = ['cat ', 'dog ', 'fish ', 'horse ', 'sheep ']
    the_list_of_lines(file_path3, lines)
    print("=="*30)


if __name__ == '__main__':
    main()

