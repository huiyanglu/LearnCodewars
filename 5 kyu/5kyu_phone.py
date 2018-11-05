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

dr = ("/+1-541-754-3010 156 Alphand_St. <J Steeve>\n 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010;\n"
"+1-541-984-3012 <P Reed> /PO Box 530; Pollocksville, NC-28573\n :+1-321-512-2222 <Paul Dive> Sequoia Alley PQ-67209\n"
"+1-741-984-3090 <Peter Reedgrave> _Chicago\n :+1-921-333-2222 <Anna Stevens> Haramburu_Street AA-67209\n"
"+1-111-544-8973 <Peter Pan> LA\n +1-921-512-2222 <Wilfrid Stevens> Wild Street AA-67209\n"
"<Peter Gone> LA ?+1-121-544-8974 \n <R Steell> Quora Street AB-47209 +1-481-512-2222!\n"
"<Arthur Clarke> San Antonio $+1-121-504-8974 TT-45120\n <Ray Chandler> Teliman Pk. !+1-681-512-2222! AB-47209,\n"
"<Sophia Loren> +1-421-674-8974 Bern TP-46017\n <Peter O'Brien> High Street +1-908-512-2222; CC-47209\n"
"<Anastasia> +48-421-674-8974 Via Quirinal Roma\n <P Salinger> Main Street, +1-098-512-2222, Denver\n"
"<C Powel> *+19-421-674-8974 Chateau des Fosses Strasbourg F-68000\n <Bernard Deltheil> +1-498-512-2222; Mount Av.  Eldorado\n"
"+1-099-500-8000 <Peter Crush> Labrador Bd.\n +1-931-512-4855 <William Saurin> Bison Street CQ-23071\n"
"<P Salinge> Main Street, +1-098-512-2222, Denve\n")

print(phone(dr, "1-098-512-2222"))