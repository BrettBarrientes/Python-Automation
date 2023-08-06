from datetime import datetime
from pathlib import Path
import os
import shutil


start_path = 'C:/Users/Documents/Old_Current_Path/' # Current Directory of the files
dest_path = 'C:/Users/Documents/New_Path/' # Directory where the files are to be moved

old_files = os.listdir(start_path)

# Moving each file under start_path to dest_path
for old_file in old_files:
    shutil.move(start_path + old_file, dest_path + old_file)

print(old_file)
print("Files have been transferred successfully!")

new_dest_path = Path(r"C:\Users\Brett\Documents\New_Path")
week_num = input("Enter the week of the Month: ")

for file in new_dest_path.iterdir():
    if file.is_file():
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

        new_directory = new_dest_path.joinpath(year_month)
        #print(new_path)
        # if not os.path.exists(new_name):
        # if the directory does not exist =>
            # create a new directory then move the files into the new directory and rename them
        if not new_directory.exists():
            new_directory.mkdir(parents=True, exist_ok=True)
            new_file_path = new_directory.joinpath(new_name)
            print(new_file_path)
            file.rename(new_file_path)
            #print(new_file_path)
        else:
            # if the directory does exist =>
                # move the files into the existing directory and rename them
            new_file_path = new_directory.joinpath(new_name)
            print(new_file_path)
            file.rename(new_file_path)
            #print(new_file_path)

print('Files have been added and renamed successfully!')
print(new_file_path)
