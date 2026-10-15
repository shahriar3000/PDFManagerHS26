import os

import config


class Organizer:

    def __init__(self):
        pass

    def organize(self, category):
        #print("Category: ", category)
        main_category, sub_category = category.rsplit(" ", 1)
        main_file = config.destinations[main_category]
        sub_file = config.endings[sub_category]
        #print("main: ", main_file)
        #print("sub: ", sub_file)
        print("file will be sent to: ", os.path.join(main_file, sub_file))

