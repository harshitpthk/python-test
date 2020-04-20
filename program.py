import sys
import re
import justext


def print_file(filename):
	f = open(filename, "rU")
	text = f.read() # string
	htmlcontent = justext.justext(text, justext.get_stoplist("English"))
	htmlcontent = htmlcontent[3:]
	htmlcontent = filter( lambda x: not x.text.isnumeric(), htmlcontent)
	
	for i in htmlcontent:
		print(i.text)

print_file("samplefile.html")
