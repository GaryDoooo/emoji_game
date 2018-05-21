import term_io
import os

def library():
    print(term_io.delete.whole_screen)
    os.system('sed -n 1,26p BookSkin')   
    term_io.press_any_key_to_continue()
    os.system('sed -n 27,52p BookSkin')
    print("\n")
    term_io.press_any_key_to_continue()

def main():
    library()
    #run_chatroom("Test")
    # print(file_num)


if __name__ == "__main__":
    main()
