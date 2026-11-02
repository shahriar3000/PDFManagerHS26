import os

import config


class Organizer:

    def __init__(self):
        pass

    def organize(self, category, year, main_file):
        #print("Category: ", category)
        main_category, semester, sub_category = category.rsplit(" ")
        sub_file = config.endings[sub_category]
        #print("main: ", main_file)
        #print("sub: ", sub_file)
        print(main_category, semester, sub_category)
        print("file will be sent to: ", os.path.join(main_file, semester + year, main_category, sub_category))

