import xml.etree.ElementTree as ET

xml = ET.parse(r'..\txt\aa.xml')
root = xml.getroot()
l = root.findall("Employee")
for element in l:
    print('tag:', element.tag, 'text:', element.text)
    print('attrib:', element.attrib['type'])
    for child in element:
        print('child tag:', child.tag, 'child text:', child.text)
