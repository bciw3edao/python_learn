def add_all(*args):
    print('------------')
    print(f'len(args)={len(args)}')
    print(f'args[0]={args[0]}')
    print(f'{20 in args}')
    #print(type(args))
    return sum(args)

print('sum(10,20)=',add_all(10, 20))
print('sum(10)=',add_all(10))
