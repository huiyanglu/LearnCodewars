"""
Extract the domain name from a URL

https://www.codewars.com/kata/514a024011ea4fb54200004b

Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"

"""

def domain_name(url):
    return url.split('//')[-1].split('www.')[-1].split('.')[0]

# 取//后面
# www.后面的关键词
# 以'.'分割
print(domain_name('http://www.youtube.com'))
