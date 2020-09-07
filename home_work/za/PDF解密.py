#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/8/30 12:14
# @Author :春衫
# @File :PDF解密.py

from PyPDF2 import PdfFileWriter, PdfFileReader

pdf_reader = PdfFileReader('encrypted.pdf')
pdf_reader.decrypt('makerbean')
pdf_writer = PdfFileWriter()
for page in range(pdf_reader.getNumPages()):
    pdf_writer.addPage(pdf_reader.getPage(page))

with open('decrypted.pdf', 'wb')as out:
    pdf_writer.write(out)
