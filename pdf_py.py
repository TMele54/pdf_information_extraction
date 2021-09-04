'''import pyPdf
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

path = "filename.pdf"
pdf = pyPdf.PdfFileReader(open(path, "rb"))
fp = file(path, 'rb')
num_of_pages = pdf.getNumPages()
extract = ""
for i in range(num_of_pages):
  inside = [i]
  pagenos=set(inside)
  rsrcmgr = PDFResourceManager()
  retstr = StringIO()
  codec = 'utf-8'
  laparams = LAParams()
  device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
  interpreter = PDFPageInterpreter(rsrcmgr, device)
  password = ""
  maxpages = 0
  caching = True
  text = ""
  for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
    interpreter.process_page(page)
    text = retstr.getvalue()
    retstr.truncate(0)
    text = text.decode("ascii","replace")
    if re.search(r"to be held (at|on)",text.lower()):
        print text
        extract = extract + text + "\n"
        continue


reader = PyPDF2.PdfFileReader('Complete_Works_Lovecraft.pdf')
reader.getPage(7-1).extractText()
my_page = reader.getPage(7)
writer.addPage(my_page)

output_filename = 'pages_we_want_to_save.pdf'
with open(output_filename, 'wb') as output: writer.write(output)
'''