# 초보자를 위한 파이썬 300제

#21
letters = 'python'
print(letters[0],letters[2])

#22
license_plate = "24가 2210"
print(license_plate[4:])
print(license_plate[-4:])

#23
string = "홀짝홀짝홀짝"
print(string[::2])

#24
string = "PYTHON"
print(string[::-1])

#25
phone_number = "010-1111-2222"
print(phone_number.replace('-',' '))
print(phone_number.replace('-',' ',2))

#26
print(phone_number.replace('-',''))

#27
url = "http://sharebook.kr"
print(url.split('.')[-1])
print(url[url.index('.')+1:])

#28
lang = 'python'
# lang[0] = 'P'
# print(lang)
# string은 immutable이라 부분 수정 불가

#29
string = 'abcdfe2a354a32a'
print(string.replace('a','A'))

#30
string = 'abcd'
string.replace('b','B')
print(string)
# aBcd