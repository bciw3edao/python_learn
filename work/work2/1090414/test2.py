def get_enconding(FileName):
    enconding_list = [None, 'ANSI', 'UTF-8', 'Big5', 'Windows-1252', 'Unicode']
    for encode in enconding_list:
        try:
            with open(FileName, encoding=encode):
                return encode
        except:
            pass


enconding = get_enconding(r'..\txt\aa.txt')
with open(r'..\txt\aa.txt', encoding=enconding) as file:
    id = input('請輸入員工編號:')
    name = input('請輸入員工姓名:')
    for chr_line in file.readlines():
        # print(chr_line.strip().split(','))
        list_line = chr_line.strip().split(',')
        if list_line[0] == id and list_line[2] == name:
            print(list_line)
