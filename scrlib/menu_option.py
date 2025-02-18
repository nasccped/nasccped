from enum import Enum

class MenuOption(Enum):
    CHECK  = (1, "check \x1b[1;32m`latest`\x1b[0m "
                 + "<-> \x1b[1;32m`all`\x1b[0m dirs")

    UPDATE = (2, "update \x1b[1;32m`dir`\x1b[0m "
                 + "content with latest ones at "
                 + "\x1b[1;32m`all`\x1b[0m")

    QUIT   = (3, "\x1b[1;31mquit\x1b[0m program")
