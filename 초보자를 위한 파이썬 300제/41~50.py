# 초보자를 위한 파이썬 300제

#41
ticker = "btc_krw"
print(ticker.upper())

#42
ticker = "BTC_KRW"
print(ticker.lower())

#43
string = "hello"
print(string.capitalize())

#44
file_name = "보고서.xlsx"
print(file_name.endswith("xlsx"))

#45
print(file_name.endswith(('xlsx','xls')))

#46
file_name = "2020_보고서.xlsx"
print(file_name.startswith('2020'))

#47
a = "hello world"
print(a.split(' '))

#48
ticker = "btc_krw"
print(ticker.split('_'))

#49
date = "2020-05-01"
ymd = date.split('-')
print('{}, {}, {}'.format(ymd[0],ymd[1],ymd[2]))

#50
data = " 039490    "
print(data.rstrip())