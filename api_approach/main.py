import json
import os
import random
import time
from tkinter import Tk
from tkinter.filedialog import askopenfilename

import pdfplumber
import PyPDF2
import requests
from dotenv import load_dotenv
from selenium import webdriver

# Load environment variables from the .env file
load_dotenv()
USER_ID = os.getenv("USER_ID_TTS")
API_KEY = os.getenv("API_KEY_TTS")


url = "https://api.play.ht/api/v2/tts"

# clone an existing audio voice or create your own!

# Existing audio: get all existing voices in the database and choose the one you like
voice_url = "https://api.play.ht/api/v2/voices"

headers = {
    "accept": "application/json",
    "AUTHORIZATION": f"{API_KEY}",
    "X-USER-ID": f"{USER_ID}",
}

response = requests.get(voice_url, headers=headers)
all_voices = response.json()
# print(data)
# now you can clone all the samples at once. First save them in a variable urls
urls = []
for voice in all_voices:
    sample_url = voice["sample"]
    urls.append(sample_url)
# print(urls)
# choose a random audio from the list or pick your own
random_audio = random.choice(urls)
url = "https://api.play.ht/api/v2/cloned-voices/instant/"

payload = f'-----011000010111000001101001\r\nContent-Disposition: form-data; name="sample_file_url"\r\n\r\n{random_audio}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name="voice_name"\r\n\r\ntest\r\n-----011000010111000001101001--\r\n\r\n'
headers = {
    "accept": "application/json",
    "content-type": "multipart/form-data; boundary=---011000010111000001101001",
    "AUTHORIZATION": f"{API_KEY}",
    "X-USER-ID": f"{USER_ID}",
}

response = requests.post(url, data=payload, headers=headers)
response_data = response.json()
id = response_data["id"]
# print(f"Id: {id}")
Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
filelocation = askopenfilename()  # open the dialog GUI, let's you choose a file

# This will splice the name of the original pdf. We will use this later to rename the mp3 file with the same name.
file_name = os.path.basename(filelocation)
name_of_file = os.path.splitext(file_name)
# Creating a PDF File Object
pdfFileObj = open(filelocation, "rb")

# creating a pdf reader object
pdfReader = PyPDF2.PdfReader(pdfFileObj)

# Get the number of pages
pages = len(pdfReader.pages)

# creates the text from the pdf file
with pdfplumber.open(filelocation) as pdf:
    string_of_text = ""
    # Loop through the number of pages
    for i in range(0, pages):
        page = pdf.pages[i]
        text = page.extract_text()
        string_of_text += text

# Generate Audio From Text
url = "https://api.play.ht/api/v2/tts"
payload = {
    "text": f"{string_of_text}",
    "voice": f"{id}",
    "quality": "draft",
    "output_format": "mp3",
    "speed": 1,
    "sample_rate": 24000,
    "seed": None,
    "temperature": None,
    "voice_engine": "PlayHT2.0",
    "emotion": "male_happy",
    "voice_guidance": 3,
    "style_guidance": 20,
}
headers = {
    "accept": "text/event-stream",
    "content-type": "application/json",
    "AUTHORIZATION": f"{API_KEY}",
    "X-USER-ID": f"{USER_ID}",
}
response = requests.post(url, json=payload, headers=headers)
time.sleep(5)
# Use splitlines() to get a list of lines

lines = response.text.splitlines()

json_like_str = lines[-2].split("data: ")[1]
data_dict = json.loads(json_like_str)

url = data_dict["url"]
# open the url
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(f"{url}")

# check if the cloned voices list is empty
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "AUTHORIZATION": f"{USER_ID}",
    "X-USER-ID": f"{API_KEY}",
}
delete_url = "https://api.play.ht/api/v2/cloned-voices/"
delete_response = requests.get(delete_url, headers=headers).json()

delete_payload = {"voice_id": f"{delete_response[0]['id']}"}
requests.delete(delete_url, json=delete_payload, headers=headers)
