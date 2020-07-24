# TODO
str_ssn = str(input())
if str_ssn[3] == '-' and str_ssn[6] == '-' \
        and str_ssn[0:3].isdigit() \
        and str_ssn[4:6].isdigit() \
        and str_ssn[7:].isdigit():
    print('Valid SSN')
else:
    print('Invalid SSN')
"""
Valid SSN
Invalid SSN
"""
