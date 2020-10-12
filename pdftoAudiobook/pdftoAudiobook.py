import PyPDF2
from gtts import gTTS 
import os 
import time

def pdf_to_audiobook(pdfname):
	language = 'en'
	file = open(pdfname, 'rb')
	fileReader = PyPDF2.PdfFileReader(file)


	finalText = ""
	for i in range(fileReader.numPages):
		a = fileReader.getPage(i)
		finalText += a.extractText()

	myobj = gTTS(text=finalText, lang=language, slow=False)
	myobj.save("{}_audiobook.mp3".format(pdfname))
	return True

def pdf_to_audiobook_per_page(pdfname):
	language = 'en'
	file = open(pdfname, 'rb')
	fileReader = PyPDF2.PdfFileReader(file)


	finalText = ""
	for i in range(fileReader.numPages):
		a = fileReader.getPage(i)
		finalText = a.extractText()

		myobj = gTTS(text=finalText, lang=language, slow=False)
		myobj.save("{}.mp3".format(i))
	return True

# print(pdf_to_audiobook('marieVF.pdf'))




# from pdftoAudiobook.pdftoAudiobook import *