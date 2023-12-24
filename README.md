# Text to Speech Conversion

This project provides two approaches for converting text to speech:

## 1. API Approach
The API approach utilizes the Play.ht Text-to-Speech API. It clones an existing audio voice or allows you to create your own, converts a PDF file's text to audio, and provides the resulting audio file.

## 2. gTTS Approach
The gTTS (Google Text-to-Speech) approach uses the gTTS library to convert text to speech. It takes a PDF file as input, extracts the text from each page, and generates corresponding audio files. The progress is displayed with a graphical progress bar.

### How to Use
1. Choose the PDF file you want to convert.
2. Select the directory to save the converted MP3 files.
3. Click "Convert to Speech" to initiate the conversion.

### Prerequisites
- Python 3
- Required libraries (install using `pip install -r requirements.txt`)

Refer to the respective folders for detailed implementation.

