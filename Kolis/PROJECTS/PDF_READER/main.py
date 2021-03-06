#!/usr/bin/env python3

import PyPDF2

pdffile = open('test.pdf', 'rb')
pdf_object = PyPDF2.PdfFileReader(pdffile)
page = pdf_object.getPage(0)
pdf_text = page.extractText()
print(pdf_text)
