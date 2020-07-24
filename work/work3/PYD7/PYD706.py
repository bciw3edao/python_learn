# TODO
list_a = list(chr(i) for i in range(ord("a"), ord("z") + 1))
set_a = set(list_a)
int_re = int(input())
while int_re >= 1:
    input_txt = input().lower()
    print(set(input_txt) >= set_a)
    int_re -= 1
