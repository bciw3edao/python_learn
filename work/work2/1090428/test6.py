from lxml import etree

xml = etree.parse(r'..\txt\aa.xml')
root = xml.getroot()
l = root.xpath("Employee[id=1]")
for element in l:
    print('tag:', element.tag, 'text:', element.text)
    print('attrib:', element.attrib['type'])
    for child in element:
        print('child tag:', child.tag, 'child text:', child.text)
