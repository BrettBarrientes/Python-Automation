import pandas as pd
import csv
import os
import shutil

# Path of the files
path_file = ("C:/Path/To/The/Folder/With/File/")
os.listdir(path_file)
# Created a empty list to store the csv files
csv_list = []

# the name of the file you want to move.
filename = 'Annual_report.csv'

# the directory in which the file is located.
current_directory = ("C:/Path/To/The/Folder/With/File/") 

# the directory in which you want to move the file.
new_directory = ("C:/Path/To/New Directory/To/Move/File/")

# Check if the file exists in the current directory.
if os.path.exists(f"{current_directory}/{filename}"):
    # Check if the file already exists in the new directory.
    if os.path.exists(f"{new_directory}/{filename}"):
        # If the file does exist, remove the old version of the file from the new directory.
        os.remove(f"{new_directory}/{filename}")
        #Print that the file already exists in the new directory, replacing the old version of the file.
        print(f"File {filename} already exists in {new_directory}, replacing existing file.")

    # After the old version of the file is removed, move the file from the current directory to the new directory.
    # Use shutil.move() to move the file from the current directory to the new directory.
    shutil.move(f"{current_directory}/{filename}", new_directory)
    #Print that the file was moved to the new directory.
    print(f"File {filename} moved to {new_directory}")

else:
    #If a new directory does not exist, create a new directory.
    os.makedirs(new_directory)
    #Print that the new directory was created.
    print(f"New directory {new_directory} created.")


# Check if to see if the files in the current directory are csv files.
    # os.listdir means it will list all the files in the current directory.
for file in os.listdir(path_file):
    if file.endswith('.csv'):
        # Print the files in the current directory.
        print('Loading file {0}.....'.format(file))
        # Append the files into the empty list
        csv_list.append(pd.read_csv(os.path.join(path_file, file)))

# Merge the files in the list into one dataframe                  
csv_merged = pd.concat(csv_list, axis = 0)

# The fileset is now ready to be exported to a csv file.
csv_merged.to_csv('Annual_report.csv', index = False)

# opening the csv file in read mode and storing it in a dataframe
df = pd.read_csv('Annual_report.csv')

# converting the date text into a datetime object under the Settlement Date column
# this will help sort the values by date with the sort function
df['Settlement Date'] = pd.to_datetime(df['Settlement Date']).dt.date

# sort dates under Settlement Date column from oldest to newest
# Note: false = newest to oldest & true = oldest to newest
df.sort_values(by = 'Settlement Date', inplace = True, ascending = True)

# Export the dataframe to a csv file
df.to_csv('Annual_report.csv', index = False)

# Print that the Annual Report is ready
print('Annual Report is ready!')












