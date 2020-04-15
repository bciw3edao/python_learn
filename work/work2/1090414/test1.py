def get_enconding(FileName):
    enconding_list = [None, 'ANSI', 'UTF-8', 'Big5', 'Windows-1252', 'Unicode']
    for encode in enconding_list:
        try:
            with open(FileName, encoding=encode):
                return encode
        except:
            pass


enconding = get_enconding(r'..\txt\txt1.txt')
with open(r'..\txt\txt1.txt', encoding=enconding) as f:
    print(f.read())
