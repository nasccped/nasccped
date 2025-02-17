
def terminal_clear():
    print("\x1b[2J\x1b[H", end="")

def print_banner():
    print("\x1b[1;37m" + ("=" * 70))
    print(
        " @"
        + "\x1b[33m" + "nasccped's "
        + "\x1b[37m" + "| "
        + "\x1b[32m" + "resumes"
    )
    print("\x1b[1;37m" + ("=" * 70))
    print("\x1b[0m")
