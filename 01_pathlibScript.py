import os
import shutil

from pathlib import Path



#targetFolder = Path(input("Please enter your targeted path: "))
targetFolder = Path(r'C:\Users\Joshua Albert\Desktop\renamingTEST - BACKUP')
searchKey = "BELLO"
replaceKey = "Ruth"



# Respond to the user with some basic information related to his hinput
print("""
Some basic information about the target you stated and the changes that will be proceeded on it:


""")
print(f"Here's the path you stated:                      '{targetFolder}' ")
print(f"Is the stated path specifying a file?            {targetFolder.is_file()}")
print(f"Is the stated path specifying a directory?       {targetFolder.is_dir()}")

# Distance for display
print("""

""")


# Set up a variable to store the number of the n-th file in the targeted folder
contentCounter = 0

# Simple loop to iterate over the target path via the '.iterdir()' method. Then, all results are printed ascending
for file in targetFolder.iterdir():
    contentCounter = contentCounter+1
    print(f"Content{contentCounter} = {file.stem}")

# Distance for display
print("""

""")


for file in targetFolder.iterdir():

    # Get the parent directory for all the files in there
    parentDirectory = file.parent

    # Get the default name of each of the files in there
    fileOriginalName = file.stem

    # Get the suffix of each of the files in there
    extension = file.suffix


    # For every original file name: Check if it contains the search term
    if searchKey in fileOriginalName:

        # Show the original name of each affected file
        print(f"Currently/Originally affected file name:                        {fileOriginalName}")

        # Set the file's new name. One variable to display it WITHOUT file-ext and one to display it WITH file-ext
        newFileNameWithoutExtension = fileOriginalName.replace(searchKey, replaceKey)
        newFileNameWithExtension = newFileNameWithoutExtension + extension

        # Print the designation-possibilities for each new file name
        print(f"NEW name for the file will be (displayed WITHOUT extension):    {newFileNameWithoutExtension}")
        print(f"NEW name for the file will be (displayed WITH extension):       {newFileNameWithExtension}")

        # Distance for displaying each affected file visually appealing
        print("""
        """)

        # Now ACTUALLY RENAME the affected files
        file.rename(Path(targetFolder, newFileNameWithExtension))

print("Done")

