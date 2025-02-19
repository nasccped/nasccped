from typing import Optional

from mods.menu_option import MenuOption

from mods.visuals import (
    terminal_clear,
    print_banner,
    print_menu_options
)

from mods.inputs import get_menu_option_by_strkey

def main():

    selected_option: Optional[MenuOption] = None

    while True:
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
        selected_option = get_menu_option_by_strkey(target_enum)

        match selected_option:
            case MenuOption.QUIT: break

    terminal_clear()
    print()
    print("  \x1b[1;31mQuitting\x1b[0m...")
    print()

if __name__ == "__main__":
    main()
