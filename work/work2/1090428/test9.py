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
# l = root.xpath('Employee[1]')  # 第1個
# l = root.xpath('Employee[position()<3]')  # 前2個
# l = root.xpath('Employee[last()]')  # 倒數第1個
# l = root.xpath('Employee[last()]')  # 倒數第2個
# l = root.xpath('Employee[@type="Programmer"]')  # 列出type="Programmer
# l = root.xpath('Employee[id>1]')  # 列出id>1
# l = root.xpath('Employee[id>1]/name')  # 列出id>1的name
# l = root.xpath('Employee[starts-with(name,"M")]')  # 列出name[0]="M"的員工資料
# l = root.xpath('Employee[id=1 and name="Mary"]')  # 列出id>1且name="Mary"的員工資料

for element in l:
    print('tag:', element.tag, 'text:', element.text)
    for child in element:
        print('child tag:', child.tag, 'child text:', child.text)
