# 초보자를 위한 파이썬 300제

#31
a = '3'
b = '4'
print(a+b)
# 34

#32
print('hi'*3)
# hihihi

#33
print('-'*80)

#34
t1 = 'python'
t2 = 'java'
print('{} {} '.format(t1,t2)*4)
print(f'{t1} {t2} '*4)
print('%s %s ' % (t1,t2)*4)

#35
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 20
print('이름: %s 나이: %s' % (name1,age1))
print('이름: %s 나이: %s' % (name2,age2))

#36
print('이름: {} 나이: {}'.format(name1,age1))
print('이름: {} 나이: {}'.format(name2,age2))

#37
print(f'이름: {name1} 나이: {age1}')
print(f'이름: {name2} 나이: {age2}')

#38
상장주식수 = "5,969,782,550"
print(int(상장주식수.replace(',','')))

#39
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])
print(분기[:분기.index('(')])

#40
data = "   삼성전자    "
print(data.strip())