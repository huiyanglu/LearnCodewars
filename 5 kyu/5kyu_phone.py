"""
Phone Directory

https://www.codewars.com/kata/56baeae7022c16dd7400086e

John keeps a backup of his old personal phone book as a text file. On each line of the file he can find the phone number (formated as +X-abc-def-ghij where X stands for one or two digits), the corresponding name between < and > and the address.

Unfortunately everything is mixed, things are not always in the same order, lines are cluttered with non-alpha-numeric characters.

Examples of John's phone book lines:

"/+1-541-754-3010 156 Alphand_St. <J Steeve>\n"

" 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010!\n"

"<Anastasia> +48-421-674-8974 Via Quirinal Roma\n"

Could you help John with a program that, given the lines of his phone book and a phone number returns a string for this number : "Phone => num, Name => name, Address => adress"

Examples:

s = "/+1-541-754-3010 156 Alphand_St. <J Steeve>\n 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010!\n"

phone(s, "1-541-754-3010") should return "Phone => 1-541-754-3010, Name => J Steeve, Address => 156 Alphand St."
It can happen that, for a few phone numbers, there are many people for a phone number -say nb- , then

return : "Error => Too many people: nb"

or it can happen that the number nb is not in the phone book, in that case

return: "Error => Not found: nb"

You can see other examples in the test cases.

JavaScript random tests completed by @matt c

Note
Codewars stdout doesn't print part of a string when between < and >

"""

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
