import os
from PyPDF2 import PdfFileReader

directory = "C:\Users\leomar\Documents\New Reports"

file = open("pdf.txt","w")

for filename in os.listdir(directory):

	pdf = PdfFileReader(open(directory + "\\" + filename,"rb"),strict=False)

	fileSize = os.path.getsize(directory + "\\" + filename)

	if pdf.isEncrypted:
		print("File is Encrypted")
	else:
		pageNumber = pdf.getNumPages()
		print(filename + ";" + str(fileSize) + ";" + str(pageNumber))
		file.write(filename + " ; " + str(fileSize) + ";" + str(pageNumber) + "\n")

file.close()