from lxml import etree

xml_str = '''
<Employees>
    <Employee type="Programmer">
		<id>1</id>
		<name>Mary</name>
	</Employee>
    <Employee type="IC Design">
		<id>2</id>
		<name>John</name>
	</Employee>
</Employees>
'''
root = etree.fromstring(xml_str)
l = root.xpath('Employee[id=1]')
for element in l:
    print('tag:', element.tag, 'text:', element.text)
    for child in element:
        print('child tag:', child.tag, 'child text:', child.text)
