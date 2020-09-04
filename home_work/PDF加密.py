#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/8/21 13:07
# @Author :春衫
# @File :PDF加密.py


from PyPDF2 import PdfFileWriter, PdfFileReader

pdf_reader = PdfFileReader('Netease Q2 2019 Earnings Release-Final.pdf')
pdf_writer = PdfFileWriter()
for page in range(pdf_reader.getNumPages()):
    pdf_writer.addPage(pdf_reader.getPage(page))

pdf_writer.encrypt('123456')
with open('encrypted.pdf', 'wb') as out:
    pdf_writer.write(out)
