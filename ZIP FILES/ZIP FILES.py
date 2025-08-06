
import zipfile
import shutil


# How to zip files together manually 
'''
zip_file = zipfile.ZipFile('excel_files.zip', 'w', zipfile.ZIP_DEFLATED)

zip_file.write('octobre.xlsx')
zip_file.write('novembre.xlsx')
zip_file.write('decembre.xlsx')

zip_file.close()
'''

# How to zip files together located in same folder automatically

shutil.make_archive('excel_files2', 'zip', 'excel_files')