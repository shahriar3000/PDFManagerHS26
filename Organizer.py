import os
import shutil
from pathlib import Path

import config


class Organizer:

    def __init__(self):
        pass

    def organize(self, category, year, main_file, file):
        destination = self.get_destination(category, year, main_file)
        #self.move_file(file, destination)
        print(destination)

    # assembles final destination address
    def get_destination(self, category, year, main_file):
        main_category, semester, sub_category = category.rsplit(" ", 2)

        destination = (
                Path(main_file)
                / f"{semester}{year}"
                / main_category
                / sub_category
        )

        return destination

    # moves the file with shutil
    def move_file(self,filepath, destination):

        filepath = Path(filepath)
        destination = Path(destination)
        destination_file = destination / filepath.name

        if destination_file.exists():
            print("File already exists!")
            return False
        try:
            shutil.move(str(filepath), str(destination_file))
            print("File moved successfully!")
            return True
        except OSError as e:
            print(f"Error when moving file: {e}")
            return False