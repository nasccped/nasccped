import re
import os

ALL_DIR    = "./all"
LATEST_DIR = "./latest"

class AllDirStatus:

    def __init__(self, pdfs_dir_path: str):

        all_f = os.listdir(pdfs_dir_path)
        regex_filter = r"^\d{4}-(en|pt)-\d{2}\.pdf$"

        self.root_path = pdfs_dir_path

        self.invalid_files_list = [
            f for f in all_f if not re.match(regex_filter, f)
        ]

        self.pdf_list = [
            f for f in all_f if f not in self.invalid_files_list
        ]

        self.eng_pdf_list = [
            f for f in self.pdf_list if f.split("-")[1] == "en"
        ]

        self.prt_pdf_list = [
            f for f in self.pdf_list if f.split("-")[1] == "pt"
        ]

        self.invalid_files_count = len(self.invalid_files_list)
        self.pdf_count           = len(self.pdf_list          )
        self.eng_pdf_count       = len(self.eng_pdf_list      )
        self.prt_pdf_count       = len(self.prt_pdf_list      )

    def show_data(self):

        i_count = self.invalid_files_count
        f_count = i_count + self.pdf_count
        e_count = self.eng_pdf_count
        p_count = self.prt_pdf_count

        print(f"  \x1b[1;32m{f_count}\x1b[0m files(s)")

        if i_count > 0:
            print(f"  | \x1b[1;31m{i_count}\x1b[0m invalid file(s)")

        print(f"  | \x1b[1;33m{e_count}\x1b[0m en pdf(s)")
        print(f"  | \x1b[1;33m{p_count}\x1b[0m pt pdf(s)")

class LatestDirStats:

    def __init__(self, pdfs_dir_path: str):

        all_f = os.listdir(pdfs_dir_path)
        regex_filter = r"^nascc-resume-(en|pt)\.pdf$"

        self.invalid_files_list = [
            f for f in all_f if not re.match(regex_filter, f)
        ]

        self.pdf_list = [
            f for f in all_f if f not in self.invalid_files_list
        ]

        self.eng_pdf_list = [
            f for f in self.pdf_list
            if f.split("-")[-1].startswith("en")
        ]

        self.prt_pdf_list = [
            f for f in self.pdf_list if f not in self.eng_pdf_list
        ]

        self.invalid_files_count = len(self.invalid_files_list)
        self.pdf_count           = len(self.pdf_list          )
        self.eng_pdf_count       = len(self.eng_pdf_list      )
        self.prt_pdf_count       = len(self.prt_pdf_list      )

    def show_data(self):

        i_count = self.invalid_files_count
        f_count = i_count + self.pdf_count
        e_count = self.eng_pdf_count
        p_count = self.prt_pdf_count

        print(f"  \x1b[1;3{1 if f_count != 2 else 2}m{f_count}\x1b[0m file(s)")

        if i_count > 0:
            print(f"  | \x1b[1;31m{i_count}\x1b[0m invalid file(s)")

        print(f"  | \x1b[1;3{1 if e_count != 1 else 3}m{e_count}\x1b[0m en pdf(s)")
        print(f"  | \x1b[1;3{1 if p_count != 1 else 3}m{p_count}\x1b[0m pt pdf(s)")

ALL_DIR_STATUS = AllDirStatus(ALL_DIR)
LATEST_DIR_STATUS = LatestDirStats(LATEST_DIR)
