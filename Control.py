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

    def startup_scan(self, watcher):

        files = watcher.scan_existing_files()

        for file in files:
            if self.classifier.created_in_year(file, "2026"):
                category = self.classifier.classify(file)

                if category:
                    self.organizer.organize(category)
            elif self.classifier.created_in_year(file, "2025"):
                print("2025", file)
            else:
                print("much older", file)




