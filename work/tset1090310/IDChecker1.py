id='A123456789'
print('EX ID:',id)
id=input('input ID:')
if len(id)!=10:
    print('長度不符合')
elif not(id.isupper()):
    print('自首不符')
elif not (id[1] in '12'):
    print('性別偵測錯誤')
elif not (id[2:].isdigit()):
    print('ID後九碼非全數字')
else:
    print('資料正確')