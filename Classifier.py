import os.path
import time

import pdfplumber
from pathlib import Path


class Classifier:

    def __init__(self, keywords):
        self.keywords = keywords

        for filename, data in keywords.items():
            required = {"category", "semester", "keywords"}

            if not required.issubset(data):
                raise ValueError(
                    f"Invalid configuration for '{filename}'."
                    f"Missing: {required - data.keys()}"
                )

    # returns
    def classify(self, file_path):
        file_name = Path(file_path).name

        #validates configuration of new data in config
        for filename_beginning, data in self.keywords.items():
            if file_name.startswith(filename_beginning):
                #print(filename_beginning)
                if self.check_keyword_PDF(file_path, data["keywords"]):
                    print(f"matching file: ", file_name, filename_beginning)
                    return data["category"]
        return None

    # opens pdf with pdfplumber and searches for words from the list given
    def check_keyword_PDF(self, file_path, keyword):
        #print(target_words)
        #print(file_path)
        try:

            with pdfplumber.open(file_path) as pdf:
                if not pdf.pages:
                    return False
                first_page = pdf.pages[0]
                text = first_page.extract_text()

                if text:
                    #checks if keyword is a single word e.g. "2026"
                    if isinstance(keyword, str):
                        if keyword in text:
                            return True
                    #checks if keyword is a list e.g. from config
                    elif isinstance(keyword, list):
                        for word in keyword:
                            if word in text:
                                return True
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

        return False

    # checks for the year of creation (download)
    def created_in_year(self, file_path, year):
        try:
            c_ti = os.path.getctime(file_path)
            c_time = time.ctime(c_ti)

            if year in c_time:
                return True
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
        return False
