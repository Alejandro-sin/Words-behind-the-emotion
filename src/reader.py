import PyPDF2
# import pandas as pd

file_object = open("./data/main/Cartas.pdf", "rb") 
reader = PyPDF2.PdfFileReader(file_object)
page1 = reader.getPage(34)
print(type(page1))

data = page1.extractText()

print(data)