import re
import os

ALL_DIR    = "all"
LATEST_DIR = "latest"

class ParentDirStatus:

    def __init__(self, dir_path: str, regex_filter: str):

        all_content = os.listdir(dir_path)
        self.root = os.path.join(".", dir_path)
        self.invalid_content = [
            ctt for ctt in all_content if not re.match(regex_filter, ctt)
        ]

        self.valid_pdfs = [
            ctt for ctt in all_content
            if ctt not in self.invalid_content
        ]


class AllDirStatus(ParentDirStatus):

    def __init__(self, dir_path: str):

        super().__init__(dir_path, r"^\d{4}-(en|pt)-\d{2}\.pdf$")

        self.eng_pdfs = [
            ctt for ctt in self.valid_pdfs
            if ctt.split("-")[1] == "en"
        ]

        self.prt_pdfs = [
            ctt for ctt in self.valid_pdfs
            if ctt not in self.eng_pdfs
        ]

    def show_data(self):

        i_count = len(self.invalid_content)
        f_count = i_count + len(self.valid_pdfs)
        e_count = len(self.eng_pdfs)
        p_count = len(self.prt_pdfs)

        print(f"    \x1b[1;32m{f_count}\x1b[0m item(s)")

        if i_count > 0:
            print(f"    | \x1b[1;31m{i_count}\x1b[0m invalid item(s):", end = " ")
            invalids = [item for item in self.invalid_content]
            if i_count > 4:
                invalids = invalids[ : 4] + [f"<+{i_count - 4} items>"]
            inv_text = ", ".join([("\x1b[1;31m" + it + "\x1b[0m") for it in invalids])
            print(inv_text)

        print(f"    | \x1b[1;33m{e_count}\x1b[0m en pdf(s)")
        print(f"    | \x1b[1;33m{p_count}\x1b[0m pt pdf(s)")

    def get_last_en_path(self) -> str:
        return os.path.join(self.root, self.eng_pdfs[-1])

    def get_last_pt_path(self) -> str:
        return os.path.join(self.root, self.prt_pdfs[-1])

class LatestDirStats(ParentDirStatus):

    def __init__(self, dir_path: str):

        super().__init__(dir_path, r"^nascc-resume-(en|pt)\.pdf$")

        self.eng_pdfs = [
            ctt for ctt in self.valid_pdfs
            if ctt.split("-")[-1].startswith("en")
        ]

        self.prt_pdfs = [
            ctt for ctt in self.valid_pdfs
            if ctt not in self.eng_pdfs
        ]

    def show_data(self):

        i_count = len(self.invalid_content)
        f_count = i_count + len(self.valid_pdfs)
        e_count = len(self.eng_pdfs)
        p_count = len(self.prt_pdfs)

        print(f"    \x1b[1;3{1 if f_count != 2 else 2}m{f_count}\x1b[0m item(s)")

        if i_count > 0:
            print(f"    | \x1b[1;31m{i_count}\x1b[0m invalid item(s):", end = " ")
            invalids = [item for item in self.invalid_content]
            if i_count > 4:
                invalids = invalids[ : 4] + [f"<+{i_count - 4} items>"]
            inv_text = ", ".join([("\x1b[1;31m" + it + "\x1b[0m") for it in invalids])
            print(inv_text)

        print(f"    | \x1b[1;3{1 if e_count != 1 else 3}m{e_count}\x1b[0m en pdf(s)")
        print(f"    | \x1b[1;3{1 if p_count != 1 else 3}m{p_count}\x1b[0m pt pdf(s)")

    def get_en_path(self) -> str:

        if len(self.eng_pdfs) != 1:
            return ""

        return os.path.join(self.root, self.eng_pdfs[0])

    def get_pt_path(self) -> str:

        if len(self.prt_pdfs) != 1:
            return ""

        return os.path.join(self.root, self.prt_pdfs[0])

def compare_files_by_path(fpath1: str, fpath2: str) -> bool:

    res = False

    try:
        with open(fpath1, "rb") as f1, open(fpath2, "rb") as f2:
            res = f1.read() == f2.read()
    except:
        return False

    return res

ALL_DIR_STATUS = AllDirStatus(ALL_DIR)
LATEST_DIR_STATUS = LatestDirStats(LATEST_DIR)
