# PDF TO AUDIOBOOK CONVERTER

This is a simple package that helps you in creating audiobooks (in the form of .mp3) from a pdf file.

## The import statement
Use this import statement to import all the functions of the library:
###### from pdftoAudiobook import *
###### Function import example: _pdftoAudiobook.pdf_to_audiobook(pdfFileName)_

# PDF TO AUDIOBOOK converter functions
There are two functions in this package:
###### pdf_to_audiobook: *This function parses through the entire pdf document, converts it into speech and creates a single .mp3 file. This function takes one string argument, the path of the pdf file that is to be converted.*
###### pdf_to_audiobook_per_page: *This function parses through the entire pdf document and creates a one .mp3 file per page. This function also takes one string argument, the path of the pdf file that is to be converted.*

# Future scopes
1. Create a function that parses through a text file and converts that into an audiobook
2. Provide another alternatives for converting text-to-speech. Currently, it uses gTTS library for this purpose.

# Limitations
1. Since gTTS library is used for text-to-speech conversion, it requires internet connection while running the scripts
2. The pdf file is converted to speech as-is, no modifications are made to the original format. Due to this, improperly
formatted file may give bad output. However with a standard text format, this will work properly.
