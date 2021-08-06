# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 15:56:22 2021

@author: joshua.albert
"""
# IMPORTANT: MOST IMPORTANT CODE LINES ARE
# "file.rename(Path(destinationFolder, newFileNameWithExtension))"
#  as well as
# "destinationFolder.mkdir(parents=True, exist_ok=True)"


from pathlib import Path
import tkinter


# Geometry and layout
window = tkinter.Tk()

window.geometry("1210x650")
window.title("rename your pictures :)")
tkinter.Label(window, text="""
    Hi :)


    This is a small tool for searching and replacing faulty sections within the names of your files. 
    It's only 6 quick steps to follow. Let's start...


    1.  Consolidate your faulty pictures in a folder and save that on your desktop.
    2.  Now open the folder via windows explorer and copy its folderpath, e.g.:  C:Users\joshua.albert\OneDrive - PUMA\Desktop\myTargetFolder
    """, anchor="w", justify="left", font='Arial 10').grid(sticky="w", row=0, columnspan=2)


# Function behind the Interface
def submit():

    # Get a value from the target entry field of the GUI by using '.get()' and turn it into a path object
    targetFolder = Path(targetFolderInput.get())

    # Get values from the search and replace entry fields of the GUI by using '.get()'
    searchKey = searchKeyInput.get()
    replaceKey = replaceKeyInput.get()

    # Get a folder name for the new file location from the now location entry field of the GUI by using'.get()'
    newLocation = newLocationInput.get()
    destinationFolder = targetFolder.joinpath(targetFolder, newLocation)


    destinationFolder.mkdir(parents=True, exist_ok=True)  # see remark the next line
    # 'parents' = True means: if necessary, create any missing (parent-) path sections
    # 'parents' = False means: raise a FileNotFoundError if a part of the parent path is missing


    # Respond to the user with some basic information related to his hinput
    print("""*** FEEDBACK BASED ON YOUR INPUT INFORMATION ***
    """)

    print(f"Here's the target path you stated:         '{targetFolder}' ")
    print(f"""Here's the destination path you defined:   '{destinationFolder}'
    
    """)
    print("The following contents were found under the path you specified:")

    #
    contentType = ""
    # Set up a variable to store the number of the n-th CONTENT in the targeted folder (may be subfolder)
    contentCounter = 0
    # Set up a variable to store the number of the n-th FOLDER in the targeted folder
    folderCounter = 0
    # Set up a variable to store the number of the n-th FILE in the targeted folder
    fileCounter = 0
    # Set up a variable to store the count of all files affected by the user's criteria
    affectedFileCount = 0



    # Count all contents in the target folder and print ther namees using the '.iterdir()' method.
    for file in targetFolder.iterdir():
        contentCounter = contentCounter + 1

        if file.is_file() == True:
            fileCounter = fileCounter + 1
            contentType = "File  "

        elif file.is_dir() == True:
            folderCounter = folderCounter + 1
            contentType = "Folder"

        print(f"Content #{contentCounter}    {contentType}    {file.stem}")

    print(f"""
That makes {contentCounter} contents:  {folderCounter} Subfolders, {fileCounter} Files.
""")



    for file in targetFolder.iterdir():

        # Get the default name of each of the files in there
        fileStemName = file.stem
        # Get the suffix of each of the files in there
        fileExt = file.suffix
        # Get the full file name INCLUDING its extension
        fileName = fileStemName + fileExt




        # For every original file name: Check if it contains the search term
        if searchKey in fileName and (file.is_file()==True):

            # Set the file's new name
            newFileName = fileName.replace(searchKey, replaceKey)
            affectedFileCount = affectedFileCount + 1

            # Print each adjustment that's going to be done
            print(f"Rename file   FROM      {fileName}     TO     {newFileName}")

            # Now ACTUALLY RENAME the affected files
            file.rename(Path(destinationFolder, newFileName))

    print(f"""CHECK IS DONE. {affectedFileCount} affected files were adjusted.""")





# Beginning of labels and entry field section here ---------------------------------------------------------------------
# Label for the target folder
targetFolderLabel = tkinter.Label(window, text="    3.  Paste the path of your targeted folder here:", anchor="w", justify="left", font='Arial 10 bold')
# Input field for the targeted path
targetFolderInput = tkinter.Entry(window, width=120, borderwidth=2, fg="blue", font="Arial 8 underline")
# Label for the search key
searchKeyLabel = tkinter.Label(window, text="    4.  Search for a faulty expression within your file names: ", anchor="w", justify="left", font='Arial 10 bold')
# Input field for the search key
searchKeyInput = tkinter.Entry(window, width=50, borderwidth=2)
# Label for the replacement key
replaceKeyLabel = tkinter.Label(window, text="    5.  What should that expression be replaced by: ", anchor="w", justify="left", font='Arial 10 bold')
# Input field for the replacement key
replaceKeyInput = tkinter.Entry(window, width=50, borderwidth=2)
# Label for the destination folder
newLocationLabel = tkinter.Label(window, width=52, text="    6.  Set a folder name for your destination folder:", anchor="w", justify="left", font='Arial 10 bold')
# Input field for the destination path
newLocationInput = tkinter.Entry(window, width=50, borderwidth=2)

# Button for executing the code
executeButton = tkinter.Button(window, text="Run the renaming >>", command=submit, font='Arial 8 bold', fg="blue")
# End of functional assignments here------------------------------------------------------------------------------------
outputResults = tkinter.Text(window, width=90, height=10, borderwidth=2)


# Start of formatting the grid here ------------------------------------------------------------------------------------
BLANK1 = tkinter.Label(window, text="").grid(row=1)  # Blank space 1
targetFolderLabel.grid(row=2, column=0, sticky="w")
targetFolderInput.grid(row=2, column=1, sticky="w")
BLANK2 = tkinter.Label(window, text="").grid(row=3)  # Blank space 2
searchKeyLabel.grid(row=4, column=0, sticky="w")
searchKeyInput.grid(row=4, column=1, sticky="w")
replaceKeyLabel.grid(sticky="w", row=5)
replaceKeyInput.grid(row=5, column=1, sticky="w")
BLANK3 = tkinter.Label(window, text="").grid(row=6)  # Blank space 3
newLocationLabel.grid(sticky="w", row=7)
newLocationInput.grid(row=7, column=1, sticky="w")
BLANK4 = tkinter.Label(window, text="").grid(row=8)  # Blank space 4
executeButton.grid(row=9, column=1, sticky="w", text=submit())
BLANK5 = tkinter.Label(window, text="").grid(row=10)  # Blank space 5
BLANK6 = tkinter.Label(window, text="").grid(row=11)  # Blank space 6
BLANK7 = tkinter.Label(window, text="").grid(row=11)  # Blank space 7

outputResults.grid(row=13, column=1)
# End of formatting the Grid here---------------------------------------------------------------------------------------



# Execute
window.mainloop()