import os
import ffmpeg
from shutil import copyfile
import sys

SRC_DIR = "example"
FILE_NAME = "test.mp3"

FILE = os.path.join(SRC_DIR,FILE_NAME)
NEW_PATH = f"{SRC_DIR}/NEW"

# Create directory
#Path(FILE).mkdir(parents=True,exist_ok=True)
# Copy file to new directory
copyfile(FILE,os.path.join(NEW_PATH,FILE_NAME))

NEW_FILE = os.path.join(NEW_PATH,"test.mp3")

DATA = ffmpeg.probe(NEW_FILE)
TITLE = DATA["format"]["tags"]["title"]
BPM:float = float(DATA["format"]["tags"]["TBPM"])
NEW_BPM = round(BPM)

print(f"File name: {NEW_FILE}")
print(f"Editing file: {TITLE}")
print(f"Changing BPM: {BPM} to {NEW_BPM}")



