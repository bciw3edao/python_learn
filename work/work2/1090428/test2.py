import xml.etree.ElementTree as ET

xmlTree = ET.parse(r'..\txt\ad.xml')
employees = xmlTree.getroot()
for employee in employees:
    print(employees.tag)
    for child_tag in employee:
        print(child_tag.tag, child_tag.text)

for employee in employees:
    print(employee.tag)
    print(employee.attrib['id'])
    print(employee.attrib['name'])

