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
    input_id = input('請輸入員工編號:')
    input_name = input('請輸入員工姓名:')

    for chr_line in file.readlines():
        # print(chr_line.strip().split(','))
        list_id, list_country, list_name = chr_line.strip().split(',')
        if list_id == input_id and list_name == input_name:
            print('ID     :', list_id, '\nCountry:', list_country, '\nName   :', list_name)
            break
