import os


for file_name in os.listdir(r"C:\Users\Admin\Downloads"):

    if not file_name.endswith(".pdf"):
        continue

