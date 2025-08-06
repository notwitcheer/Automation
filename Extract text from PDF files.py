# Extract text from PDF files.

from PyPDF2 import PdfFileWriter, PdfFileReader

f = open('QuickStart-FicheRecap.pdf', 'rb')

reader = PdfFileReader(f)
page0 = reader.getPage(0)
text = page0.extractText()
text = text.replace('Ò', '"').replace('”', 'é').replace('Õ', '\'').replace('¥', '- ')
print(text)

f.close()