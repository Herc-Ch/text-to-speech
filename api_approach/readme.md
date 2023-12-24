# Text-to-Speech Conversion with Play.ht API

## Overview

This Python script utilizes the Play.ht API to convert text from a PDF file into speech. It includes functionality to clone an existing audio voice or create a new one. The script then generates audio from the PDF text, allowing the user to choose a PDF file for conversion.

## Prerequisites

1. Python 3.x
2. Install required Python packages using:

    ```bash
    python -m pip install -r requirements.txt
    ```

    On MacOS, use `pip3` instead of `pip`.

3. Set up the required environment variables in a `.env` file:

    ```env
    USER_ID_TTS=your_user_id
    API_KEY_TTS=your_api_key
    ```
    You can generate your own at this address [PlayHT](https://play.ht/studio/api-access)

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/text-to-speech.git
    ```

2. Navigate to the project folder:

    ```bash
    cd text-to-speech/api_approach
    ```

3. Install dependencies:

    ```bash
    python -m pip install -r requirements.txt
    ```

4. Run the script:

    ```bash
    python main.py
    ```

## Features

- Choose a PDF file for text-to-speech conversion.
- Clone an existing audio voice or create a new one.
- Convert each page of the PDF into an individual MP3 file.
- Open the generated audio in a web browser.

## Project Structure

1. `text_to_speech_playht.py`: Main Python script for text-to-speech conversion.
2. `requirements.txt`: List of Python packages required for the project.
3. `.env`: Configuration file for storing environment variables.
4. `README.md`: Documentation file (you're reading it!).

## Dependencies

- **pdfplumber:** A library for extracting text from PDF files.
- **PyPDF2:** A library for reading PDF files and extracting text.
- **requests:** Library for making HTTP requests.
- **dotenv:** Module for reading environment variables from a file.
- **selenium:** Web browser automation library.

## Usage

1. Run the script.
2. Choose a PDF file for conversion.
3. Clone an existing audio voice or create a new one.
4. Open the generated audio in a web browser.


## Acknowledgments

- [pdfplumber](https://github.com/jsvine/pdfplumber)
- [PyPDF2](https://pypdf2.readthedocs.io/en/3.0.0/)
- [requests](https://docs.python-requests.org/en/latest/)
- [dotenv](https://pypi.org/project/python-dotenv/)
- [selenium](https://www.selenium.dev/)
