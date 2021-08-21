# 초보자를 위한 파이썬 300제

#71
my_variable = ()
print(my_variable,type(my_variable))

#72
movie_rank = ('닥터 스트레인지', '스플릿','럭키')
print(movie_rank,type(movie_rank))

#73
t = (1,)
print(t,type(t))
t = 1,
print(t,type(t))
# 만약 t = (1)로 선언하면 int형으로 저장됨.
t = (1)
print(t,type(t))

#74
t = (1,2,3)
#t[0] = 'a'
# tuple은 요소를 변경할 수 없어 오류 발생

#75
t = 1,2,3,4
print(t, type(t))
# ()치거나 안치거나 값이 여러가지면 tuple형

#76
t = ('a','b','c')
t = ('A','b','c')
print(t)

#77
interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest = list(interest)
print(interest, type(interest))

#78
interest = tuple(interest)
print(interest,type(interest))

#79 언패킹
temp = ('apple','banana','cake')
a,b,c = temp
print(a,b,c)
# apple banana cake

#80
t = tuple(range(2,100,+2))
print(t,type(t))

t = tuple(x for x in range(1,100) if x % 2 ==0)
print(t,type(t))