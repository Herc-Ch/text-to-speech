# PDF to Speech Conversion

## Overview

This simple Python application converts text from a PDF file to speech using the gTTS (Google Text-to-Speech) library. It provides a graphical user interface (GUI) to select a PDF file, choose the output directory, and convert each page of the PDF into an individual MP3 file.

## Prerequisites

1. Python 3.x
2. Install required Python packages using:

    ```bash
    python -m pip install -r requirements.txt
    ```

    On MacOS, use `pip3` instead of `pip`.

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/Herc-Ch/text-to-speech.git
    ```

2. Navigate to the project folder:

    ```bash
    cd text-to-speech
    ```

3. Install dependencies:

    ```bash
    python -m pip install -r requirements.txt
    ```

4. Run the application:

    ```bash
    python gtts/main.py
    ```

    The application will open a GUI for PDF to Speech Conversion.

## Features

- Choose a PDF file for conversion.
- Select the output directory for the converted MP3 files.
- Monitor the progress with a graphical progress bar.
- Receive completion message after the conversion.

## Project Structure

1. `pdf_to_speech.py`: Main Python script for PDF to Speech Conversion.
2. `requirements.txt`: List of Python packages required for the project.
3. `README.md`: Documentation file (you're reading it!).

## Dependencies

- **PyPDF2:** A library for reading PDF files and extracting text.
- **gTTS (Google Text-to-Speech):** A library for interacting with Google Text-to-Speech API.
- **tkinter:** Standard GUI toolkit for Python.

## Usage

1. Run the application.
2. Choose the PDF file you want to convert.
3. Select the directory to save the converted MP3 files.
4. Click "Convert to Speech" to initiate the conversion process.


## Acknowledgments

- [PyPDF2](https://pypdf2.readthedocs.io/en/3.0.0/)
- [gTTS (Google Text-to-Speech)](https://gtts.readthedocs.io/en/latest/)
