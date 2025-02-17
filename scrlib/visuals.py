from .menu_options import MenuOptions

def terminal_clear():
    print("\x1b[2J\x1b[H", end="")

def print_banner():
    print("\x1b[1;37m" + ("=" * 70))
    print(
        "  @"
        + "\x1b[33m" + "nasccped's "
        + "\x1b[37m" + "| "
        + "\x1b[32m" + "resumes"
    )
    print("\x1b[1;37m" + ("=" * 70))
    print("\x1b[0m")

def print_menu_options():
    
    men_opt = {
        str(opt.value[0]) + "." : opt.value[1] for opt in MenuOptions
    }

    for (k, v) in men_opt.items():
        print(
            "  "
            + "\x1b[1;33m" + k + " "
            + "\x1b[0m"    + v
        )
