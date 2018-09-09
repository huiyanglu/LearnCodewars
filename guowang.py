from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from random import randint
from selenium.webdriver.support.select import Select


browser = webdriver.Chrome("/usr/local/bin/chromedriver") #打开浏览器
wait=WebDriverWait(browser,10) # 显示等待，最长10秒

browser.get('https://w.wjx.top/m/27515749.aspx#') #请求链接

rawFirst='''
1-5    D B A C B 
6-10   C B B A B 
11-15  C A D A D 
16-20  A B B D B 
21-25  C C A C A 
26-30  B A B A C 
31-35  B A D A C 
36-40  D A B A D 
41-45  A B A A C 
46-50  A B B D A 
51-55  B B C B D 
56-60  A B C B A 
61-65  D B A B C 
66-70  D B A C A 
71-73  B D C  
'''.split(" ")

rawSecond='''
74-78    ABCDE  ABC   ABD     ABCD   ABCD 
79-83    BCD    ABCD  ABCDEF  ACDE  ABCE 
84-88    ABCD   ABCD  ABDE    ABCD  BCDE 
89-93    ABDE   ABC    BCDE   ABD   ABC 
94-98    ABCE   ABCDF  ACDE   ABC   ABCDE 
99-103   ABCDE  ABCD   ABCDE  ABCD  ABD 
104-108  ABC    ABCD   BCD    ABCDE  ABD 
109-110  ABCD   BCD  
'''.split(" ")
firstList=[]
secondList=[]

# 填写省份城市
xpath='//*[@id="div1"]/div[2]'
browser.find_element_by_xpath(xpath).click() #对象定位
browser.switch_to_frame(0)
Select(browser.find_element_by_id("province")).select_by_value("江苏") #通过id定位元素
Select(browser.find_element_by_id("city")).select_by_value("扬州市")
Select(browser.find_element_by_id("area")).select_by_value("广陵区")
browser.find_element_by_xpath('/html/body/div/div[5]/a').click()

# 填写公司
xpath='//*[@id="div2"]'
browser.find_element_by_xpath(xpath).click()
browser.switch_to_frame(0)
Select(browser.find_element_by_xpath('/html/body/div/div[1]/div/select')).select_by_index("2") #按顺序选择 index从0开始
Select(browser.find_element_by_xpath('/html/body/div/div[2]/div/select')).select_by_index("8")
browser.find_element_by_xpath('/html/body/div/div[5]/a').click()

# 填写公司
xpath='//*[@id="q3_1"]'
browser.find_element_by_xpath(xpath).send_keys("国网扬州供电公司")
# 填写手机
xpath='//*[@id="q3_2"]'
phone="159052737"+ str(randint(1,99))
browser.find_element_by_xpath(xpath).send_keys(phone)


for c in rawFirst:
    if c in ["A","B","C","D"]:
        firstList.append(c)
for c in rawSecond:
    for c2 in ["A","B","C","D"]:
        if c2 in c:
            secondList.append(c)
            break
dct={"A":1,"B":2,"C":3,"D":4,"E":5}
firstList=map(lambda x:dct[x],firstList)
firstList=list(firstList)
for question in range(1,74):
    xpath='//*[@id="div'+str(question+3)+'"]/div[2]/div['+str(firstList[question-1])+']'
    browser.find_element_by_xpath(xpath).click()

for question in range(74,111):
    for ans in secondList[question-74]:
        ans = ord(ans)-64
        xpath='//*[@id="div'+str(question+3)+'"]/div[2]/div['+str(ans)+']'
        browser.find_element_by_xpath(xpath).click()