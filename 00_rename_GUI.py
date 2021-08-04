# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 15:56:22 2021

@author: joshua.albert
"""
from pathlib import Path
#from pathlibFirstSuccessfulFunction import rename_pictures

import tkinter

window = tkinter.Tk()
window.geometry("1380x450")
window.title("rename your pictures :)")


tkinter.Label(window, text="""
    Hi :)


    This is a small tool for searching and replacing faulty sections in the designation of your images. Let's start...


    Step 1:  Consolidate your faulty pictures in a folder and save that on your desktop.
    Step 2:  Now open the folder via windows explorer and copy its folderpath, e.g.:  C:Users\joshua.albert\OneDrive - PUMA\Desktop\pyTestForRenaming
""", anchor="w", justify="left", font='Arial 10').grid(sticky="w", row=0, columnspan=2)


def submit():

    targetFolder = Path(targetFolderInput.get())
    searchKey = searchKeyInput.get()
    replaceKey = replaceKeyInput.get()


    # Respond to the user with some basic information related to his hinput
    print("""
Some basic information about the target you stated and the changes that will be proceeded on it:


    """)

    print(f"Here's the path you stated:                      '{targetFolder}' ")
    print(f"Is the stated path specifying a file?            {targetFolder.is_file()}")
    print(f"Is the stated path specifying a directory?       {targetFolder.is_dir()}")

    # Distance for display
    print("""


The following contents were found under the path you specified:""")

    # Set up a variable to store the number of the n-th file in the targeted folder
    contentCounter = 0

    # Simple loop to iterate over the target path via the '.iterdir()' method. Then, all results are printed ascending
    for file in targetFolder.iterdir():
        contentCounter = contentCounter + 1
        print(f"Content #{contentCounter}    {file.stem}")

    # Distance for display
    print("""

    """)

    for file in targetFolder.iterdir():

        # Get the parent directory for all the files in there
        # parentDirectory = file.parent

        # Get the default name of each of the files in there
        fileOriginalName = file.stem

        # Get the suffix of each of the files in there
        extension = file.suffix

        # For every original file name: Check if it contains the search term
        if searchKey in fileOriginalName:
            # Show the original name of each affected file
            print(f"Currently/Originally affected file name:                {fileOriginalName}")

            # Set the file's new name. One variable to display it WITHOUT file-ext and one to display it WITH file-ext
            newFileNameWithoutExtension = fileOriginalName.replace(searchKey, replaceKey)
            newFileNameWithExtension = newFileNameWithoutExtension + extension

            # Print the designation-possibilities for each new file name
            print(f"NEW name for the file (displayed WITHOUT extension):    {newFileNameWithoutExtension}")
            print(f"NEW name for the file (displayed WITH extension):       {newFileNameWithExtension}")

            # Distance for displaying each affected file visually appealing
            print("""
            """)

            # Now ACTUALLY RENAME the affected files
            file.rename(Path(targetFolder, newFileNameWithExtension))

    done = "done"

    if not searchKey in fileOriginalName:
        print("NO FILES AFFECTED BY YOUR SEARCH TERM :)")

    return (done)


# Labels and entry fields section starts here -------------------------------------------------------------------------

# Label for the target folder
targetFolderLabel = tkinter.Label(window, text="    Step 3: Paste the path of your targeted folder here:", anchor="w", justify="left", font='Arial 10 bold')
# Input field for the targeted path
targetFolderInput = tkinter.Entry(window, width=120, borderwidth=2, fg="blue", font="Arial 8 underline")

# Label for the search key
searchKeyLabel = tkinter.Label(window, text="    Step 4:  Search for a faulty expression your picture designations here: ", anchor="w", justify="left", font='Arial 10 bold')
# Input field for the search key
searchKeyInput = tkinter.Entry(window, width=50, borderwidth=2)

# Label for the replacement key
replaceKeyLabel = tkinter.Label(window, text="    Step 5:  What should that expression be replaced by: ", anchor="w", justify="left", font='Arial 10 bold')
# Input field for the replacement key
replaceKeyInput = tkinter.Entry(window, width=50, borderwidth=2)

# Label for the destination folder
destinationLabel = tkinter.Label(window, width=65, text="    Step 6:  Set a name for the destination folder of your adjusted files:", anchor="w", justify="left", font='Arial 10 bold')
# Input field for the destination path
destinationFolder = tkinter.Entry(window, width=50, borderwidth=2)

# Button for executing the code
executeButton = tkinter.Button(window, text="Run the renaming >>", command=submit, font='Arial 8 bold', fg="blue")


# Formatting the grid here ---------------------------------------------------------------------------------------------
BLANK1 = tkinter.Label(window, text="").grid(row=1)  # Blank space 1

targetFolderLabel.grid(row=2, column=0, sticky="w")
targetFolderInput.grid(row=2, column=1, sticky="w")

BLANK2 = tkinter.Label(window, text="").grid(row=3)  # Blank space 2

searchKeyLabel.grid(row=4, column=0, sticky="w")
searchKeyInput.grid(row=4, column=1, sticky="w")

replaceKeyLabel.grid(sticky="w", row=5)
replaceKeyInput.grid(row=5, column=1, sticky="w")

BLANK3 = tkinter.Label(window, text="").grid(row=6)  # Blank space 3

destinationLabel.grid(sticky="w", row=7)
destinationFolder.grid(row=7, column=1, sticky="w")

BLANK4 = tkinter.Label(window, text="").grid(row=8)  # Blank space 4
BLANK5 = tkinter.Label(window, text="").grid(row=9)  # Blank space 5

executeButton.grid(row=15, column=1, sticky="w")


# Execute
window.mainloop()