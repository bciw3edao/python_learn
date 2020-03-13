def add(a:int,b:int)->int:
    if not isinstance(a,int):
        print('a ro b not int')
        return None
    return a + b


print(add('1',1))
x= lambda a,b:a+b
print(x(1,2))
