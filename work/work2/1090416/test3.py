import csv

input_id = input('input User   ID:')
input_name = input('input User NAME:')

with open(r'..\txt\ab.txt') as f:
    data = csv.DictReader(f)
    for z in data:
        if input_id == z['id'] and input_name == z['name']:
            print('ID     :', z['id'], '\nname   :', z['name'], '\naddress:', z['address'])
            break
    else:
        print('Not Found')
