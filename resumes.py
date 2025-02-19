from typing import Optional
from mods.menu_option import MenuOption
from mods.visuals import (
    terminal_clear,
    print_banner,
    print_menu_options
)
from mods.inputs import get_menu_option_by_strkey
from mods.tasks import (
    ALL_DIR_STATUS,
    LATEST_DIR_STATUS,
    compare_files_by_path,
    replace_pdfs
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
                print(f"\x1b[1;3{2 if en_upd else 1}m{'Yes' if en_upd else 'No. (May not exists)'}\x1b[0m")
                print("  - latest pt pdf is updated:", end = " ")
                print(f"\x1b[1;3{2 if pt_upd else 1}m{'Yes' if pt_upd else 'No. (May not exists)'}\x1b[0m")
                print()

                input("  Press Enter ")
                selected_option = None

            case MenuOption.UPDATE:
                if not ALL_DIR_STATUS.is_safe_update() or not LATEST_DIR_STATUS.is_safe_update():
                    print("  \x1b[1;37mThe resume pdfs \x1b[31mcouldn't be updated\x1b[37m!")
                    print("  " + ("-" * 36) + "\x1b[0m")
                    print("    Possible causes are:")
                    print(
                        "      - Expecting pdfs at \x1b[1;32m`latest`\x1b[0m dir, "
                        + "but they \x1b[1;31mdoesn't exist\x1b[0m"
                    )
                    print(
                        "      - Invalid items at \x1b[1;32m`all/latest`\x1b[0m dir "
                        + "\x1b[1;31m(no regex matches)\x1b[0m"
                    )
                    print(
                        "      - Files/Dirs \x1b[1;31mnot found\x1b[0m. Probably doesn't exists",
                        end = "\n\n"
                    )
                    print("  Consider fix this \x1b[1;33mmanually\x1b[0m!", end = "\n\n")

                else:
                    already_update = compare_files_by_path(
                        ALL_DIR_STATUS.get_last_en_path(), LATEST_DIR_STATUS.get_en_path()
                    )
                    already_update = already_update and compare_files_by_path(
                        ALL_DIR_STATUS.get_last_pt_path(), LATEST_DIR_STATUS.get_pt_path()
                    )

                    if already_update:
                        print("  \x1b[1;37mThe resume pdfs \x1b[31mcouldn't be updated\x1b[37m!")
                        print("  " + ("-" * 36) + "\x1b[0m")
                        print("    They're \x1b[1;32malready updated\x1b[0m...")
                        print()

                    else:
                        last_en = LATEST_DIR_STATUS.get_en_path()
                        all_en = ALL_DIR_STATUS.get_last_en_path()
                        last_pt = LATEST_DIR_STATUS.get_pt_path()
                        all_pt = ALL_DIR_STATUS.get_last_pt_path()

                        print(f"  `{last_en}` will be replaced by `{all_en}`.", end = " ")

                        if input("\x1b[1;33mAre you sure?\x1b[0m [y/n] ") == "y":
                            replace_pdfs(last_en, all_en)
                            print("    \xb1[1;32m> Replaced\x1b[0m")
                        else:
                            print("    \x1b[1;31m> Aborted\x1b[0m")

                        print(f"  `{last_en}` will be replaced by `{all_en}`.", end = " ")

                        if input("\x1b[1;33mAre you sure?\x1b[0m [y/n] ") == "y":
                            replace_pdfs(last_en, all_en)
                            print("    \xb1[1;32m> Replaced\x1b[0m")
                        else:
                            print("    \x1b[1;31m> Aborted\x1b[0m")

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
