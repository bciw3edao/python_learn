id = 'A111111111'
print('EX ID:',id)
id=input('input ID:')
if len(id) == 10:
    print('ID長度正確')
    if id.isupper():
        if id[1:].isdigit() == True:
            print('ID字首正確')
            if id[1] == '1':
                print('性別:男')
            elif id[1] == '2':
                print('性別:女')
            else:
                print('性別偵測錯誤\n請重新輸入ID')
        else:
            print('ID後九碼皆為數字\n請重新輸入ID')
    else:print('ID字首英文為大寫\n請重新輸入ID')
else:
    print('ID輸入錯誤(長度錯誤)')
