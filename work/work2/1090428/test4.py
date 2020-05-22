import xml.etree.ElementTree as ET

xmlTree = ET.parse(r'..\txt\ae.xml')
employees = xmlTree.getroot()

for employee in employees:
    print(employee.tag)
    print(employee.attrib['id'])
    print(employee.attrib['name'])