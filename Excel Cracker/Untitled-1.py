from openpyxl import load_workbook

dir_file_path = '/Volumes/GoogleDrive/My Drive/Monash/ENG0002/Excel Cracker/sample.xlsx'

workbook = load_workbook(dir_file_path)

workbook.security.lockStructure = False

workbook.save(dir_file_path)
workbook.close()