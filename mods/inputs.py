from typing import Optional
from .menu_option import MenuOption

def get_menu_option_by_strkey(key: str) -> Optional[MenuOption]:
    
    for enum in MenuOption:
        if key == str(enum.value[0]):
            return enum
