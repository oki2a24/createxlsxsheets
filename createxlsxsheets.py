from openpyxl import Workbook
wb = Workbook ()
dest_filename = 'サンプル.xlsx'
prefix = 'シート'
serial_numbers = range(1, 55)
for serial_number in serial_numbers:
    wb.create_sheet (title='{0}{1}'.format (prefix, serial_number))
wb.save(filename = dest_filename)
