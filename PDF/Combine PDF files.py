# Combine PDF files.

from PyPDF2 import PdfFileWriter, PdfFileReader

output_source = PdfFileWriter()

file_QuickStart_FicheRecap = open('QuickStart-FicheRecap.pdf', 'rb')
file_Publication_Kivy_Android_Google_Play = open('Publication-Kivy-Android-Google-Play.pdf', 'rb')


reader_QuickStart_FicheRecap = PdfFileReader(file_QuickStart_FicheRecap)
reader_Publication_Kivy_Android_Google_Play  = PdfFileReader(file_Publication_Kivy_Android_Google_Play)

print('page number:' + str(reader_QuickStart_FicheRecap.getNumPages()))
print('page number:' + str(reader_Publication_Kivy_Android_Google_Play.getNumPages()))

output_source.addPage(reader_QuickStart_FicheRecap.getPage(0)) # .rotateClockwise(90)
for i in range(reader_Publication_Kivy_Android_Google_Play.getNumPages()):
    output_source.addPage(reader_Publication_Kivy_Android_Google_Play.getPage(i))


output_file = open('output.pdf', 'wb')
output_source.write(output_file)
output_file.close() 

file_QuickStart_FicheRecap.close()
file_Publication_Kivy_Android_Google_Play.close()