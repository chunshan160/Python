#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/8/20 22:29
# @Author :春衫
# @File :PDF加水印.py

from copy import copy
from PyPDF2 import PdfFileWriter, PdfFileReader

watermark_paf = PdfFileReader('水印.pdf')
watermark_page = watermark_paf.getPage(0)
pdf_reader = PdfFileReader('Netease Q2 2019 Earnings Release-Final.pdf')
pdf_writer = PdfFileWriter()

#对每一页循环加水印
for page in range(pdf_reader.getNumPages()):
    #获取页面内容
    original_page = pdf_reader.getPage(page)
    #copy水印
    new_page = copy(watermark_page)
    #加水印 水印在底
    new_page.mergePage(original_page)
    #加到pdf_writer里面，等待后续处理
    pdf_writer.addPage(new_page)

with open('watermarked.pdf', 'wb') as out:
    pdf_writer.write(out)
