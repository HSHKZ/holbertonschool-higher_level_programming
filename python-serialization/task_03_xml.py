#!/usr/bin/env python3
'''3. Serializing and Deserializing with XML'''


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    '''serialize the dictionary into XML and\\
        save it to the given filename'''
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    '''Parse the XML file using ET.parse'''
    tree = ET.parse(filename)
    root = tree.getroot()
    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text
    return dictionary
