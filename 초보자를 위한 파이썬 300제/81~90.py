# 초보자를 위한 파이썬 300제

#81
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*a, _,_ = scores
print(a)

#82
_,_,*c = scores
print(c)

#83
_,*b,_ = scores
print(b)

#84
temp = {}
print(temp,type(temp))
temp = dict()
print(temp,type(temp))

#85
ice = {'메로나':1000,'폴라포':1200,'빵빠레':1800}
print(ice,type(ice))
ice2 = dict(메로나=1000,폴라포=1200,빵빠레=1800)
print(ice2,type(ice2))

#86
ice['죠스바'] = 1200
ice['월드콘'] = 1500
print(ice)
ice3 = dict(죠스바=1200,월드콘=1500)
ice2.update(ice3)
print(ice2)

#87
print(f'메로나 {ice["메로나"]}')
print(f"메로나 {ice['메로나']}")

#88
ice['메로나']=1300
print(ice)

#89
del(ice['메로나'])
print(ice)
ice2.pop('메로나')
print(ice2)

#90
#ice['누가바']
# 없는 key 값을 인덱싱하면 에러 발생