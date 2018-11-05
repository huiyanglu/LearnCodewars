import re

def domain_name(url):
    mod_url = re.sub(r'[^A-Za-z0-9\+\-\<\>\.\']|/d+',' ',url)
    name1 = mod_url.split('<')[-1].split('>')[0]
    return 'Name => ' + name1

def domain_phone(url):
    mod_url = re.sub(r'[^A-Za-z0-9\+\-\<\>\.\']|/d+', ' ', url)
    del_name = mod_url.split('<')[0] + mod_url.split('>')[-1]
    phone1 = del_name.split('+')[-1].split(' ')[0]
    return phone1

def domain_address(url):
    mod_url = re.sub(r'[^A-Za-z0-9\+\-\<\>\.\']|/d+', ' ', url)
    del_name = mod_url.split('<')[0] + mod_url.split('>')[-1]
    mod_add = del_name.split('+')[0]+del_name.split('+')[-1].split(' ', 1)[-1]
    x = re.split(r'[^A-Za-z0-9\-\.\']+', mod_add.strip())
    add1 = ' '.join(x)
    return 'Address => '+add1

def phone(strng,num):
    split_strng = re.split(r'\n', strng.strip())
    count = 0
    for each_strng in split_strng:
        each_phone = domain_phone(each_strng)
        if each_phone == num:
            count += 1
            rst_strng = each_strng
    if count>1:
        return 'Error => Too many people: ' + num
    elif count == 0:
        return 'Error => Not found: '+ num
    else:
        phone = 'Phone => '+domain_phone(rst_strng)
        name = domain_name(rst_strng)
        addr = domain_address(rst_strng)
        rst = phone+', '+name+', '+addr
        return str(rst)
