# given solution
# https://www.codewars.com/kata/5ab23a9c1cec39668c000055/solutions/python

date_validator = (
    '((('
    '(0[1-9]|1\d|2[0-8])\.(0[1-9]|1[012])|'    # 01-28 of any month
    '(29|30)\.(0[13-9]|1[012])|'               # 29-30 of months, except February
    '(31\.(0[13578]|1[02])))\.'                # 31 of long months
    '([1-9]\d{3}|\d{3}[1-9]))|'                # any year, except 0000
    '(29\.02\.('                               # leap day
    '\d\d([2468][048]|[13579][26]|0[48])|'     # leap years (mod 4)   
    '([2468][048]|[13579][26]|0[48])00'        # leap years (mod 400)
    ')))$' )
