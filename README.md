# Python Automated Transfer Scripts

1. Summary of the file_transfer_script 
  - The script's job is to move the files from one directory to another then rename the files according to the number of week in the month       that its in.
  - Once the script determines the week # by the user, the script will finish adding the week # to the file.
  - Now if the week # directory exists, those files will be moved to the folder associated to the week # of the files.
    -- If the week # does not exist, a directory will be made with the week number and those files will be moved or directed to that new   
        folder directory of the week that   was determined. 
--Purpose--
#Saves time on renaming and moving the folders to their respective destination according to the week in the month.
#Saves about 30 minutes a week => Saves 2 to 2.5 hours a month of productive work being done depending how many files need to be moved. 

2. Summary of the transfer_script_boto3 script:
   - Transfer script (transfer_script_boto3) is mainly used for objects to be transferred from one bucket to another for different paths in 
      AWS S3 using boto3.
   - The other script (transfer_script) is used if you want to use your local machine to transfer files from one directory to another then 
      renaming the files if you had a list of the directories path in excel.
--Purpose--
#Saves a few days of manuel work especially when all the paths in the S3 bucket are different. 
