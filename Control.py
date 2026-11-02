import config
from Watcher import Watcher
from Classifier import Classifier
from Organizer import Organizer
from config import keywords
import os
import time

class Control:

    def __init__(self):
        self.Running = True
        self.classifier = Classifier(keywords)
        self.organizer = Organizer()

    def run(self):
        watcher = Watcher(self)
        self.startup_scan(watcher)
        watcher.run()

    def file_created(self, filepath):

        if filepath.endswith(".pdf"):
            category = self.classifier.classify(filepath)
            if category:
                #Organizers turn
                self.organizer.organize(category)
                pass
            else:
                print("Category couldn't be matched")

#TODO: Make startup scan find out the year of the pdf by scanning inside or outside, then give it to organize
    def startup_scan(self, watcher):

        files = watcher.scan_existing_files()

        for file in files:

            if file.endswith(".pdf"):

                if self.classifier.check_keyword_PDF(file, "2026"):
                    year = "26"
                elif self.classifier.created_in_year(file, "2026"):
                    year = "26"
                elif self.classifier.check_keyword_PDF(file, "2025"):
                    year = "25"
                elif self.classifier.created_in_year(file,"2025"):
                    year = "25"
                else:
                    continue

                category = self.classifier.classify(file)
                main_file = config.main_directory[year]

                if category:
                    self.organizer.organize(category, year, main_file)





