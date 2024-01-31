a = 10
print(a)

a= 20
print(a)

b = 30
print(b)

print('hello world')

#엄청나게 빠르게 성장하기 위한 데브코드를 작성하자
# git을 자유자재로 사용하기 위해 진심으로 노력하자


name  = "mike"

print(name)

city = 'seoul'
print(city)


#리스트 
names = ['mike','jane','tom']
print(names)


#리스트에 있는 값을 불러오기 위해서는 index를 활용한다
print(names[0])
print(names[1])
print(names[2])

#이미 for문 안에 names 라는 리스트를 지정해 주었으니
# print단계에서 names를 다시 한번 지정하지 않는다.
for i in names:
    print(i)

#딕셔너리
#이걸로 묶어서 DB로 활용할 수 있을 것이다
#기본 개념들 가볍게 여기지 말고 집중해서 잘 해보자
    
user ={}#딕셔너리를 사용하려면 이런식으로 미리 설정을 해줘야한다. 다른 변수들과 다르다
user['age'] = 25
user['address'] = 'seoul'

print(user)
print(user['age'])#이런식으로 정확하게 짚어서 데이터를 추출하고 사용할 수 있다
print(user.get('age'))#방법은 많다 get을 사용해서 뽑아낼수도 있다
user['age'] = 90
print(user.get('age'))


#왜 업로드가 안되는 것일까?

###좀 되라!



#if문 활용
#python에서는 자바와 다르게 if문 for문 뒤에 :를 붙여서 사용한다
name ='jane'
if name =='jane':
    print('이름은 jane')
else:
    print("not jane")


age = 35
if age>30 : 
    print('30살보다 많습니다')
else: 
    print('30살보다 적습니다')

odd_number = [1, 3, 5, 7, 9, 11, 13]

for num in odd_number : #num은 odd_number에 있는 변수
    print(odd_number)
#한개씩 출력하려면 어케야하지?


for num in odd_number : #num은 odd_number에 있는 변수
    print(num) #이렇게 하면 한개씩 출력할 수 있다.

print("=====================================================")

#짝수만 출력하는 함수
numbers = [1,2,3,4,5,6,7]

for num in numbers:#num은 numbers안에 있는 변수이다
    if num %2 ==0:
        print(num)


print("=====================================================")

ages = [10,21,25,33,44,55,66]

for i in ages:
    print(i)
    if i>30:
        print("break")
        break


print("=====================================================")

# c언어 java에서 우리가 흔히 사용하는 for문을 구현하기 위해서는 range를 이용해야한다
add =0

for i in range(1,11): #이렇게하면 1부터 10까지 포함되는것이다,맨 처음은 포함되도 맨 마지막은 포함 안되네?
    add = add + i
    print(i)
    print(add)
print(add)

# for i in range(1,21)


add =0
for i in range(1,11):
    add = add + 1
    print(i)
    print(add)
print(add)


