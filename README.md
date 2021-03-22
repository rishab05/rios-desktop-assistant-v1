# rios-desktop-assistant-v1
A desktop assistant which can automate daily life task like opening websites in browser, open programs, type some notes in text file, play music, search Wikipedia and many more

## Requirements
Python 3.6 or later
Pyttsx3
Pyaudio
Speech recognition
Wikipedia

run "pip install requirements.txt" to install all module

<br/>
If any error occurs due to pyaudio then please go to the repo directory and run "pip install PyAudio-0.2.11-cp39-cp39-win_amd64.whl"
If you have 32 bit system or using Linux or MAC then please refer below link
https://stackoverflow.com/questions/54998028/how-do-i-install-pyaudio-on-python-3-7

## Features
* Play Music  - please change your directory(line 90)
* Send Emai - Provide your email and password in sendEmail function and reciever id at line 107. You can create a dictionary for your contacts too.
* Type notes - File will be saved in notes folder. You can change the location
* Open Google in browser
* Open Youtube
* Open StackOverflow
* Open Visual studo code - change the path
* Tell the Current Time
* Search wikipedia and read output
