def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    # your code here
    lst = []
    for i in range(a,b+1):
        if if_true(i):
            lst.append(i)
    return lst

def if_true(num):
    num2 = num
    i = len(str(num))
    s = 0
    while num2!=0:
        mod = num2%10
        num2//=10
        s+=mod**i
        i-=1
    if(s==num):
        return True
    else:
        return False
