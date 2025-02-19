import re
import os

ALL_DIR    = "./all"
LATEST_DIR = "./latest"

class ParentDirStatus:

    def __init__(self, dir_path: str, regex_filter: str):

        all_content = os.listdir(dir_path)

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

        print(f"  \x1b[1;32m{f_count}\x1b[0m files(s)")

        if i_count > 0:
            print(f"  | \x1b[1;31m{i_count}\x1b[0m invalid file(s)")

        print(f"  | \x1b[1;33m{e_count}\x1b[0m en pdf(s)")
        print(f"  | \x1b[1;33m{p_count}\x1b[0m pt pdf(s)")

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

        print(f"  \x1b[1;3{1 if f_count != 2 else 2}m{f_count}\x1b[0m file(s)")

        if i_count > 0:
            print(f"  | \x1b[1;31m{i_count}\x1b[0m invalid file(s)")

        print(f"  | \x1b[1;3{1 if e_count != 1 else 3}m{e_count}\x1b[0m en pdf(s)")
        print(f"  | \x1b[1;3{1 if p_count != 1 else 3}m{p_count}\x1b[0m pt pdf(s)")

ALL_DIR_STATUS = AllDirStatus(ALL_DIR)
LATEST_DIR_STATUS = LatestDirStats(LATEST_DIR)
