from typing import Optional
from .menu_option import MenuOption

def get_menu_option_by_strkey(key: str) -> Optional[MenuOption]:
    
    if not key.isnumeric():
        return None

    key = int(key)

    for enum in MenuOption:
        if key == enum.value[0]:
            return enum
