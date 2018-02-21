#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
import json
from bs4 import BeautifulSoup
import urllib.request

input_file = open("sample.tsv", "r")
path = "all_transcriptsUND/"

for row in input_file:
    text = ''
    row_elements = row.split("\t")
    url = re.sub(r"\n", "", row_elements[5])
    page = urllib.request.urlopen(url).read()
    page_json = json.loads(page.decode('utf-8'))
    for element in page_json:
        text += element["text"] + " "

    text = re.sub(r"\n", " ", text)
    text = re.sub(r"\s+", " ", text)

    output_file = open(path + row_elements[0] + "_" + row_elements[1] + "_" + row_elements[2] + "_" + row_elements[3] + "_" + row_elements[4]+".txt","w")
    output_file.write("<doc discipline=" + '"' + row_elements[0] + '"' + " ")
    output_file.write("sub_discipline=" + '"' + row_elements[1] + '"' + " ")
    output_file.write("topic=" + '"' + row_elements[2] + '"' + " ")
    output_file.write("author=" + '"' + row_elements[3] + '"' + " ")
    output_file.write("video_title=" + '"' + row_elements[4] + '"' + " ")
    output_file.write("transcript_url=" + '"' + url + '"' + ">\r\n")
    output_file.write(text)
    output_file.write("\r\n</doc>")
    output_file.close()
