from lxml import etree

with open(r'..\txt\aa.xml', encoding='UTF-8') as f:
    data = f.readlines()
    print(type(data))
    root = etree.fromstringlist(data)
    l = root.xpath('Employee[id=1]')
    for element in l:
        print('tag:', element.tag, 'text:', element.text)
        for child in element:
            print('child tag:', child.tag, 'child text:', child.text)
