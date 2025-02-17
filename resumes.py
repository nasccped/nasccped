from scrlib.visuals import (
    terminal_clear,
    print_banner,
    print_menu_options
)

from scrlib.inputs import get_menu_option_by_strkey

def main():
    terminal_clear()
    print_banner()
    print(
        "  \x1b[1;37m" + "Choose an option"
    )
    print(
        "  ----------------"
        + "\x1b[0m"
    )
    print_menu_options()
    print()
    target_enum = input("  > ")
    target_enum = get_menu_option_by_strkey(target_enum)
    print()
    print(
        "  You selected "
        + ("\x1b[1;31mNone" if target_enum is None else ("\x1b[1;34m" + target_enum.name))
        + "\x1b[0m"
    )
    print()

if __name__ == "__main__":
    main()
