input_id = input('input User ID:')
input_name = input('input User NAME:')
with open(r'..\txt\aa.txt') as f:
    l = f.readlines()


    def filter(data):
        id, country, name = data.strip().split(',')
        if id == input_id and name == input_name:
            return True
        else:
            return False


    matches = [x.strip() for x in l[1:] if filter(x)]
    if len(matches) > 0:
        print(matches)
    else:
        print('Not Found')
