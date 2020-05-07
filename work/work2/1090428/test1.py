import xml.etree.ElementTree as ET

employees = ET.Element('Employees')
employee1 = ET.SubElement(employees, 'Employee')
id1 = ET.SubElement(employee1, 'id')
id1.text = '1'
name1 = ET.SubElement(employee1, 'name')
name1.text = 'Mary'

employee1 = ET.SubElement(employees, 'Employee')
id1 = ET.SubElement(employee1, 'id')
id1.text = '1'
name1 = ET.SubElement(employee1, 'name')
name1.text = 'Mary'

print(ET.tostring(employees))
et = ET.ElementTree(employees)
with open(r'..\txt\ae.xml', 'wb') as f:
    et.write(f, encoding='UTF-8')
