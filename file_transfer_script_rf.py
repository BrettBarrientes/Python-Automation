import os
import shutil
from pathlib import Path
from datetime import datetime

def move_files(start_path, dest_path):
    old_files = os.listdir(start_path)

    for old_file in old_files:
        shutil.move(os.path.join(start_path, old_file), os.path.join(dest_path, old_file))

    print("Files have been transferred successfully!")

def rename_and_move_files(new_dest_path, week_num):
    new_dest_path = Path(new_dest_path)

    for file in new_dest_path.iterdir():
        if file.is_file():
            directory = file.parent
            extension = file.suffix

            old_name = file.stem
            region, report_type, old_date = old_name.split('-')

            old_date = datetime.strptime(old_date, '%Y%b%d')
            date = datetime.strftime(old_date, '%b')

            new_name = f'{region}-{date}-{report_type}-{week_num}{extension}'
            year_month = datetime.strftime(old_date, "%Y-%b")

            new_directory = new_dest_path.joinpath(year_month)

            if not new_directory.exists():
                new_directory.mkdir(parents=True, exist_ok=True)
            
            new_file_path = new_directory.joinpath(new_name)
            print(new_file_path)
            file.rename(new_file_path)

    print('Files have been added and renamed successfully!')
    print(new_file_path)

if __name__ == "__main__":
    start_path = 'C:/Users/Documents/Old_Current_Path/'
    dest_path = 'C:/Users/Documents/New_Path/'

    move_files(start_path, dest_path)

    new_dest_path = "C:/Users/Brett/Documents/New_Path"
    week_num = input("Enter the week of the Month: ")

    rename_and_move_files(new_dest_path, week_num)
