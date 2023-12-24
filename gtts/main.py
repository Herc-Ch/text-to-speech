import os
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askdirectory, askopenfilename
from tkinter.messagebox import showinfo

import PyPDF2
from gtts import gTTS

"""
On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
"""
# GUI part
root = tk.Tk()
root.geometry("400x150")
root.title("PDF to Speech Conversion")


# Function to display an information message
def show_info_message(message):
    showinfo("Information", message)


# Display initial instructions
show_info_message("Choose the PDF file you want to convert.")
filelocation = askopenfilename()  # open the dialog GUI, let's you choose a file

# This will splice the name of the original pdf. We will use this later to rename the mp3 file with the same name.
file_name = os.path.basename(filelocation)
name_of_file = os.path.splitext(file_name)
# name_of_file[0] will give you the name only

# Creating a PDF File Object
pdfFileObj = open(filelocation, "rb")

# creating a pdf reader object
pdfReader = PyPDF2.PdfReader(pdfFileObj)

# Get the number of pages
pages = len(pdfReader.pages)

# Ask for the directory only once
show_info_message("Choose the directory to save the converted MP3 files.")
output_path = askdirectory()


def update_progress_label():
    return f"Current Progress: {progress_var.get():.2f}%"


def convert_to_speech(page_number=0):
    if page_number < pages:
        page = pdfReader.pages[page_number]
        text = page.extract_text()
        final_file = gTTS(text=text, lang="en")
        final_file.save(f"{output_path}/(Audio){name_of_file[0]}_{page_number + 1}.mp3")

        progress_var.set(((page_number + 1) / pages) * 100)  # Update progress
        value_label["text"] = update_progress_label()

        # Schedule the next page conversion after 1000 milliseconds (1 second)
        root.after(1000, convert_to_speech, page_number + 1)
    else:
        showinfo(message="PDF to speech conversion completed!")
        root.destroy()


# progressbar
progress_var = tk.DoubleVar()
pb = ttk.Progressbar(
    root, orient="horizontal", mode="determinate", length=380, variable=progress_var
)
# place the progressbar
pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)

# label
value_label = ttk.Label(root, text=update_progress_label())
value_label.grid(column=0, row=1, columnspan=2)

# start button
start_button = ttk.Button(
    root, text="Convert to Speech", command=lambda: convert_to_speech(0)
)
start_button.grid(column=0, row=2, padx=10, pady=10, sticky=tk.E)

root.mainloop()
