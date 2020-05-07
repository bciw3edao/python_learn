import xml.etree.ElementTree as ET

employees = ET.Element('Employees')
employee1 = ET.SubElement(employees, 'Employee')
employee1.set('id', '1')
employee1.set('name', 'Mary')

employee2 = ET.SubElement(employees, 'Employee')
employee2.set('id', '2')
employee2.set('name', 'Jhon')

print(ET.tostring(employees))
et = ET.ElementTree(employees)
with open(r'..\txt\ae.xml', 'wb') as f:
    et.write(f, encoding='UTF-8')
