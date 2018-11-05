import re

def increment_string(s):
    number = re.findall(r'\d+', s) #找到所有数字
    if number:
        lst = number[-1]
        s = s.rsplit(lst, 1)[0] # 从右向左找最后一个数，取除最后一个数以外的前面部分
        number = str(int(lst) + 1) # 先把最后一个数转为数字，加1，再转为字符串（过程中lst的位数会变化）
        return s + '0' * (len(lst) - len(number)) + number #转换中少掉的0要补上
    else:
        return s + '1'