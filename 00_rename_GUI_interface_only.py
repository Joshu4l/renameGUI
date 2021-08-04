# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 15:56:22 2021

@author: joshua.albert
"""

import tkinter

window = tkinter.Tk()

# Set the GUI window's size
window.geometry("1380x450")

# Give the window a title
window.title("rename your pictures :)")


# Create 
tkinter.Label(window, text = """
    Hi :)
    

    This is a small tool for searching and replacing faulty sections in the designation of your images. Let's start...
    
    
    Step 1:  Consolidate your faulty pictures in a folder and save that on your desktop.
    Step 2:  Now open the folder via windows explorer and copy its folderpath, e.g.:  C:Users\joshua.albert\OneDrive - PUMA\Desktop\pyTestForRenaming
"""
, anchor = "w", justify = "left", font='Arial 10').grid(sticky = "w", row = 0, columnspan = 2)




# Create an empty row as a distancing blank space
tkinter.Label(window, text = "").grid(row = 1) # blank space on in row 2


# Input section for the targeted folder's location 
tkinter.Label(window, text = "    Step 3: Paste the path of your targeted folder here:", anchor = "w", justify = "left", font='Arial 10 bold').grid(sticky = "w", row = 2)
entryText = tkinter.StringVar()
targetFolderInput = tkinter.Entry(window, textvariable = entryText, width = 120, borderwidth= 2, fg = "blue", font = "Arial 8 underline").grid(row = 2, column = 1, sticky = "w")
entryText.set("e.g.:  C:Users\joshua.albert\OneDrive - PUMA\Desktop\myFaultyImages")



# Create an empty row as a distancing blank space
tkinter.Label(window, text = "").grid(row = 3)




# Input section for the destination folder's location
tkinter.Label(window, text = "    Step 4:  Search for a faulty expression your picture designations here: ", anchor = "w", justify = "left", font='Arial 10 bold').grid(sticky = "w", row = 4)
searchForInput = tkinter.Entry(window, width = 50, borderwidth= 2).grid(row = 4, column = 1, sticky = "w")

# Input section for the targeted folder's location 
tkinter.Label(window, text = "    Step 5:  What should that expression be replaced by: ", anchor = "w", justify = "left", font='Arial 10 bold').grid(sticky = "w", row = 5)
replaceByInput = tkinter.Entry(window, width = 50, borderwidth= 2).grid(row = 5, column = 1, sticky = "w")




# Create two empty rows as a distancing blank space
tkinter.Label(window, text = "").grid(row = 6)




# Input section for the destination folder's location
tkinter.Label(window, width = 65, text = "    Step 6:  Set a name for the destination folder of your adjusted files:", anchor = "w", justify = "left", font='Arial 10 bold').grid(sticky = "w", row = 7)
destinationFolderInput = tkinter.Entry(window, width = 50, borderwidth= 2).grid(row = 7, column = 1, sticky = "w")


# Create two empty row to separate the user's input from the next button
tkinter.Label(window, text = "").grid(row = 8)
tkinter.Label(window, text = "").grid(row = 9)




#tkinter.Button(window, text = "Next >>", command = DataCamp_Tutorial).grid(row = 2, column = 1)
tkinter.Button(window, text = "Run the renaming >>", font='Arial 8 bold', fg = "blue").grid(row = 15, column = 1, sticky = "w")


# Execute
window.mainloop()


# VARIABLES SO FAR
# targetFolderInput
# searchForInput
# replaceByInput
# destinationFolderInput