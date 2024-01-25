#
import os
from lxml import etree

XML_BASE = '../DATA'
PRES_XML_PATH = os.path.join(XML_BASE, 'presidents.xml')

pres_doc = etree.parse(PRES_XML_PATH)

for president in pres_doc.findall('.//president'):
    pres_party = president.find('party').text
    if pres_party == 'Whig':
        pres_name = president.find('name')
        pres_fname = pres_name.find('first').text
        pres_lname = pres_name.find('last').text
        print(pres_fname, pres_lname)
