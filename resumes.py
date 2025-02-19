from typing import Optional
from mods.menu_option import MenuOption
from mods.visuals import (
    terminal_clear,
    print_banner,
    print_menu_options
)
from mods.inputs import get_menu_option_by_strkey
from mods.tasks import (
    ALL_DIR_STATUS, LATEST_DIR_STATUS, compare_files_by_path
)

def main():

    selected_option: Optional[MenuOption] = None

    while True:

        terminal_clear()
        print_banner()

        match selected_option:

            case MenuOption.QUIT:
                break

            case MenuOption.CHECK:
                print("  \x1b[1;32m`all`\x1b[37m dir status")
                print("  ----------------" + "\x1b[0m")
                ALL_DIR_STATUS.show_data()
                print()

                print("  \x1b[1;32m`latest`\x1b[37m dir status")
                print("  -------------------" + "\x1b[0m")
                LATEST_DIR_STATUS.show_data()
                print()

                en_upd = compare_files_by_path(
                    ALL_DIR_STATUS.get_last_en_path(),
                    LATEST_DIR_STATUS.get_en_path()
                )
                pt_upd = compare_files_by_path(
                    ALL_DIR_STATUS.get_last_pt_path(),
                    LATEST_DIR_STATUS.get_pt_path()
                )

                print("  - latest en pdf is updated:", end = " ")
                print(f"\x1b[1;3{2 if en_upd else 1}m{en_upd}\x1b[0m")
                print("  - latest pt pdf is updated:", end = " ")
                print(f"\x1b[1;3{2 if pt_upd else 1}m{pt_upd}\x1b[0m")
                print()

                input("  Press Enter ")
                selected_option = None

            case _:
                print("  \x1b[1;37m" + "Choose an option")
                print("  ----------------" + "\x1b[0m")
                print_menu_options()
                print()
                target_enum = input("  > ").strip()
                selected_option = get_menu_option_by_strkey(target_enum)

    terminal_clear()
    print()
    print("  \x1b[1;31mQuitting\x1b[0m...")
    print()

if __name__ == "__main__":
    main()
