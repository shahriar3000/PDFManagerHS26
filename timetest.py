import os
import time

path = r"C:\Users\Admin\Downloads\ex02.pdf"

c_ti = os.path.getctime(path)

clear_time = time.ctime(c_ti)

if "2026" in clear_time:
    print(clear_time)