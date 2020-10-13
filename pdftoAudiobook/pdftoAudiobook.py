import PyPDF2
from gtts import gTTS 
import os 
import time

def pdf_to_audiobook(pdfname):
	"""
	Takes one string argument, that is, pdf file path name and 
	returns an audiobook as a single .mp3 file
	"""
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
	"""
	Take one string argument pdf file, that is, pdf file path name and
	returns one .mp3 file per page. 
	"""
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