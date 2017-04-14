import xlsxwriter

#creating a workbook and saving it in a specific directory that we want
workbook = xlsxwriter.Workbook('result.xlsx')
#creating a worksheet in the workbook
worksheet = workbook.add_worksheet()

# Widen the first column to make the text clearer.
worksheet.set_column('A:A', 20)
worksheet.set_column('B:B', 100)

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})
# Write some data headers.
worksheet.write('A1', 'Date', bold)
worksheet.write('B1', 'Reviews', bold)

#initialising the rows and colss
row = 1
col = 0

for item in range(1,4):
	worksheet.write(row,col, item)
	row+=1
workbook.close()

print "End of xlsxwriter"
