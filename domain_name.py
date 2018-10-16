def domain_name(url):
    return url.split('//')[-1].split('www.')[-1].split('.')[0]

# 取//后面
# www.后面的关键词
# 以'.'分割
print(domain_name('http://www.youtube.com'))
