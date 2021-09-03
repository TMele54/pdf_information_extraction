reader = PyPDF2.PdfFileReader('Complete_Works_Lovecraft.pdf')
reader.getPage(7-1).extractText()
my_page = reader.getPage(7)
writer.addPage(my_page)

output_filename = 'pages_we_want_to_save.pdf'
with open(output_filename, 'wb') as output:
    writer.write(output)