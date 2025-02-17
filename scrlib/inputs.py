from typing import Optional
from .menu_options import MenuOptions

def get_menu_option_by_strkey(key: str) -> Optional[MenuOptions]:
    
    if not key.isnumeric():
        return None

    key = int(key)

    for enum in MenuOptions:
        if key == enum.value[0]:
            return enum
