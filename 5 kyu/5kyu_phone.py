"""
Phone Directory
https://www.codewars.com/kata/566584e3309db1b17d000027/solutions/python

John keeps a backup of his old personal phone book as a text file. On each line of the file he can find the phone number (formated as +X-abc-def-ghij where X stands for one or two digits), the corresponding name between < and > and the address.

Unfortunately everything is mixed, things are not always in the same order, lines are cluttered with non-alpha-numeric characters.

Examples of John's phone book lines:

"/+1-541-754-3010 156 Alphand_St. \n"

" 133, Green, Rd. NY-56423 ;+1-541-914-3010!\n"

" +48-421-674-8974 Via Quirinal Roma\n"

Could you help John with a program that, given the lines of his phone book and a phone number returns a string for this number : "Phone => num, Name => name, Address => adress"
"""
import re

def phone(strng,num):
    if strng.count('+'+num)==0:
        return 'Error => Not found: ' + num
    elif strng.count('+'+num)>1:
        return 'Error => Too many people: ' + num
    for line in strng.splitlines():
        if '+' + num in line:
            name1 = re.sub('.*<(.*)>.*', '\g<1>', line)
            mod_url = re.sub('<' + name1 + '>|\+' + num, '', line)
            x = re.split(r'[^A-Za-z0-9\-\.\']+', mod_url.strip())
            add1 = ' '.join(x)
            return 'Phone => %s, Name => %s, Address => %s' %(num,name1,add1)

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

print(phone(dr, "1-931-512-4855"))