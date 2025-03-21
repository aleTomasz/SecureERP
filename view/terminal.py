import os
import time


def clear(s):
    time.sleep(s)
    os.system("cls||clear")


def print_menu(title, list_options):
    print(f"{title}:\n")
    for i in range(0, len(list_options)):
        if i != 0:
            print(f"({i}) {list_options[i]}")
    for i in range(0, len(list_options)):
        if i == 0:
            print(f"({i}) {list_options[i]}")
    print()


def print_message(message):
    print(f"{message}\n")


def print_general_results(result, label):
    if type(result) == int:
        print(f"{label}:\n\n{result}")
    elif type(result) == float:
        print(f"{label}:\n\n{format(result, '.2f')}")
    elif type(result) == list:
        print(f"{label}:")
        print()
        for i in result:
            print(f"{i}")
    elif type(result) == tuple:
        result = list(result)
        print(f"{label}:")
        print()
        for i in result:
            print(f"{i}")
    elif type(result) == dict:
        print(f"{label}:")
        print()
        for key, value in result.items():
            print(f"{key}: {value}")
    input("")


def print_table(table):
    separator = " | "
    line_separator = "-" * 31
    content = ""
    for row in table:
        line = ""
        for item in row:
            if item != row[-1]:
                line += f"{separator[1:]}{item:^30}"
            else:
                line += f"{separator[1:]}{item:^30}{separator[:-1]}"
        if row != table[-1]:
            content += f"{line}\n"
            content += f"{('|' + line_separator) * len(table[0])}"
            content += f"{'-|'}\n"
        else:
            content = f"{content}{line}"
    print(f"/{'-' * (len(line) - 2)}\\")
    print(f"{content}")
    print(f"\\{'-' * (len(line) - 2)}/")
    input("")


def get_input(label):
    inp = input(f"{label}:\n- ")
    clear(0)
    return inp


def get_inputs(labels):
    inputs = []
    for label in labels:
        inputs.append(input(f"{label}:\n- "))
    clear(0)
    return inputs


def print_error_message(message):
    print(f"Error: {message}\n")
