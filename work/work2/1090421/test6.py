with open(r'..\txt\ac.txt') as f:
    import json

    fileStr = json.loads(f.read())
    input_id = input('input User ID:')
    input_name = input('input User NAME:')
    for jsonStr in fileStr:
        if jsonStr['id'] == int(input_id) and jsonStr['name'] == input_name:
            print('id  :', jsonStr['id'], '\nname:', jsonStr['name'])
            break
    else:
        print('NotFind')
