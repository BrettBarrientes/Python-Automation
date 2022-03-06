from datetime import datetime
from pathlib import Path
import os
import shutil


our_files = Path(r"C:\Users\Brett\Documents\Python")

new_new_path = Path(r"C:\Users\Brett\Documents")
##print(our_files)
week_num = input("Enter the week of the Month: ")

for file in our_files.iterdir():
    #if file.is_file():
        directory = file.parent
        extension = file.suffix

        old_name = file.stem
        region, report_type, old_date = old_name.split('-')

        old_date = datetime.strptime(old_date, '%Y%b%d')
        date = datetime.strftime(old_date, '%b')

        ##print(date)

        new_name = f'{region}-{date}-{report_type}-{week_num}{extension}'

        #print(new_name)

        year_month = datetime.strftime(old_date, "%Y-%b")

        new_path = our_files.joinpath(year_month)
        #print(new_path)
        if not os.path.exists(new_name):

            if not new_path.exists():
                new_path.mkdir(parents=True, exist_ok=True)


        new_file_path = new_path.joinpath(new_name)
        #print(new_file_path)
        file.rename(new_file_path)

shutil.move(new_path, new_new_path)
