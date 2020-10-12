from setuptools import setup, find_packages

with open('README.md') as readme_file:
	README = readme_file.read()

setup_args = dict(
	name='pdfToAudioBookConverter',
	version='0.0.1',
	description='This package converts a pdf file to audiobooks',
	long_description_content_type="text/markdown",
	long_description=README,
	license='MIT',
	packages=find_packages(),
	author='Rahul Mishra',
	author_email='rahulmishra.psy@gmail.com',
	keywords=['Audiobooks', 'pdf', 'audiobookconverter'],
	url='https://github.com/seigfried1/pdftoaudiobook',
)

install_requires = [
	'gTTS>=2.1.1',
	'PyPDF2>=1.26.0'
]