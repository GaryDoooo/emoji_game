import os
import term_io


def welcome_print():
    print(term_io.bgcolor.black +term_io.fgcolor.Yellow)
    os.system("figlet 'Game of the EMOJI       '")
    print(term_io.bgcolor.black+term_io.fgcolor.default)
    print("Version 0.3")
    print("   by DOOOOM and Libbzy" + "\n")


def main():
    welcome_print()


if __name__ == "__main__":
    main()
