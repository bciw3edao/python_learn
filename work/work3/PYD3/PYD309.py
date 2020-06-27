# TODO
user_input_Amount = eval(input())
user_input_rate_of_return = eval(input())
user_input_Month = eval(input())

# 此為格式化輸出之標頭
print('%s \t  %s' % ('Month', 'Amount'))
# TODO
total = user_input_Amount
for i in range(1, user_input_Month + 1):
    # 此為格式化輸出之內容，需置於置於迴圈中
    total = total + total*(user_input_rate_of_return) / 1200
    print('%3d \t %.2f' % (i, total))
