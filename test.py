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

#function 
def add(x,y,z):# 변수설정까지 파이썬 정말로 간편하다...!
    return x+y+z

result = add(10,30,50)
print(result)

def subtract(x,y):
    return x-y

result  = subtract(20,10)
print(result)

def multifly(w,x,y,z):
    return w*x*y*z

result = multifly(2,3,4,5)
print(result)
print(multifly(10,20,30,40))#이런식으로도 활용 가능하다


#함수를 항상 만들필요 없이 파이썬 내장함수 쓰면 ㅈㄴ편하게 할 수 있다

a = "Good Morning, man"
a.upper()#all 대문자로 바꿔준다
print(a)#적용되서 저장까지 이어지는것은 아니다
print(a.upper())

a.lower()
a.count('m')#m이 몇개나 있는지 세준다

a = "Life is too short"
print(a)
a.replace("Life","Your height")
print(a)



#왜그런지 모르겠는데 파이썬 내장함수들이 사용이 안된다
#정확히는 적용이 안된다

#오늘의 결론
#리스트[],딕셔너리{},for i in range(1,11),for i in ages:
# 반복문과 함수 뒤에 :를 붙이고 함수는 def, return 으로 값을 돌려받는다
#DUSI가 안되더라도 분명 파고들 수 있는 공간이 있을것이다 
#낙심하지말고 전진 ㄱㄱ

#github DESKTOP덕분에 git문제가 급한불은 끈 것처럼 보이지만, 남의 코드와 합치고 하려면
#아무래도 sourcetree가 필수적일듯하다..
#아는만큼 보이는 법이니 공부해서 더 좋은 방향으로 나아가보도록 한다

name = 'jane'
if name =='jane':
    print("이름은 제인")
else:
    print("not jane")


age = 35
if age >30:
    print("30이상")
elif age>40:
    print("40이하")
else:
    
    print("30이하")



odd_number = [1,3,5,7,9,11,13]

for num in odd_number:
    print(num)

ages = [10,21,25,33,44,55,66]
for i in ages:
    if i>30:
        print("stop")
        break


add =0
for i in range(1,11): #이렇게하면 1부터 10까지 포함되는것이다,맨 처음은 포함되도 맨 마지막은 포함 안되네?
    add = add + i
    print(i)
    
print(add)

def add(x,y,z):
    return x+y+z

result = add(10,30,50)
print(result)

a = "Good morning, man"
print(a.upper())
print(a.count("m"))
print(a.split())


a = ("10"+"01")
print(a)
print(type(a))

a = int("10"+"01")
print(a)
print(type(a))

a=0
while a <10:
    a = a+1
    if a%2 ==0: continue#a가 짝수이면 print(a)가 실행되지 않는다
    print(a)


# treehit = 0
# while treehit <10:
#     treehit = treehit + 1
#     print("나무를 %d번 찍습니다" %treehit)
#     if treehit ==10:
#         print("나무가 넘어갑니다~~~!")

# for i in range(1,11):
#     print("나무를 %d번 찍습니다" %i)

# print("나무가 넘어갑니다~~~!")


# coffee= 10
# while True:
#     money = int(input("돈을 넣어주세요:"))
#     if money ==300:
#         print("커피를 줍니다")
#         print("남은 커피의 양은 %d개 입니다" %coffee)
#         coffee = coffee -1
    
#     elif money>300:
#         print("거스름돈 %d를 주고 커피를 줍니다" %(money-300))
#         print("남은 커피의 양은 %d개 입니다" %coffee)

#         coffee = coffee -1
    
#     else:
#         print("돈을 다시 돌려주고 커피를 주지 않습니다")
#         print("남은 커피의 양은 %d개 입니다" %coffee)
    
#     if coffee ==0:
#         print("커피가 다 떨어졌습니다")
#         break


# while a <10:
#     a = a+1
#     if a%2 ==0: continue
#     print(a)



# while True:
#     print("CTRL+C를 눌러 탈출")
    


def add_mul(choice,*args):#여러개의 매개변수를 이런식으로 받을 수 있다
    if choice =="add":
        result = 0
        for i in args:
            result = result +i
    
    elif choice =="mul":
        result =1 
        for i in args:
            result = result *i

    return result

result = add_mul("add",1,2,3,4,5)
print(result)

print("here")

result = add_mul("mul",1,2,3,4,5)
print(result)

def print_kwargs(**kwargs):
    print(kwargs)



print(print_kwargs(a=1))


# A,B = input().split()
# print(int(A)+int(B))
# print(int(A)-int(B))
# print(int(A)*int(B))
# print(int(A)/int(B))
# print(int(A)%int(#))

#백준 2587
# A = int(input())

# if A<1000:
#     print("잘못 입력")
# elif A>3000:
#     print("잘못 입력")

# print(A-543)


#백준 2588

# %연산자: 나눗셈 후 나머지를 리턴
# // 연산자: 나눗셈 후 몫을 리턴

# A = int(input())
# B = int(input())

# a1 = A%10
# a2 = (A%100)//10
# a3 = A//100

# b1 = B%10
# b2 = (B%100)//10
# b3 = B//100

# print(A*b1)
# print(A*b2)
# print(A*b3)
# print(A*B)

#백준 11382
#split을 사용하게되면 문자열로 인식한다
# A,B,C = input().split()
#그렇기에 int를 붙여서 정수형으로 형변환 시켜준다
# a = int(A)
# b = int(B)
# c = int(C)

# print(a+b+c)

print("\\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \(__)|")

#1330
# A,B = input().split()
# a = int(A)
# b = int(B)


# if(a>b):
#     print('>')
# elif(a<b):
#     print('<')
# else:
#     print('==')


#9498


# a= int(input())

# if a>=90:
#     print("A")
# elif a>=80:
#     print("B")
# elif a>=70:
#     print("C")
# elif a>=60:
#     print("D")        
  
# else:
#     print("F")


#2753
# year = int(input())

# if ((year%4 ==0) and (year%100 !=0) or (year%400 ==0)):#파이썬 코드는 되게 직관적이구나....
#     print(1)
# else:
#     print(0)


#14681
    

# x = int(input())
# y = int(input())


# if(x>0):
#     if(y>0):
#         print(1)
#     else:
#         print(4)

# else:
#     if(y>0):
#         print(2)
#     else:
#         print(3)


    
#2884번
# H,M = input().split()
# h = int(H)
# m = int(M)

# if m<45:
#     if(h==0):
#         h=23
#         m+=60
#     else:
#         h-=1
#         m+=60
# print(h,m-45)


# def clock(h,m):
#     if(m<45):
#         temp_h = h-1
#         temp_m += 60
#         print("%d  %d",temp_h,temp_m)

# #0시일떄 경우의수
#     elif h == 0:
#         temp_h = 23
#         temp_m = 60-m-45
#         print("%d  %d",temp_h,temp_m)

#     else:
#         temp_m = m-45
#         print("%d  %d",temp_h,temp_m)

# clock(h,m)



# H,M = input().split()
# h = int(H)
# m = int(M)

# n = int(input())#need time(요리하는데 필요한 시간)

# h += n//60
# m += n%60

# if(m>=60):#60분을 넘어가면
#     m -= 60
#     h+=1
# if(h>=24):#24시를 넘어가면
#     h-=24

# print(h,m)


# A,B,C = input().split()
# a = int(A)
# b = int(B)
# c = int(C)


# if(a==b==c):#세개가 같을 경우
#     print(10000+a*1000)
# elif(a==b) or (a==c) or (b==c):#두개가 같을 경우
#     if(a==b) or (a==c):# a와 b가 같을경우
#         print(1000 + a*100)
#     else:# b c 가 같을경우
#         print(1000 + b*100)
# else:#모두 다를 경우
#     if(a>b) and (a>c):
#         print(a*100)
#     elif(b>a) and (b>c):
#         print(b*100)
#     else:
#         print(c*100)








n= int(input())
for i in range(1,10):
    print(n, '*' , i ,'=', n*i)
# print("%d * %d = %d",a,i,a*i)




#n+m이 60을 넘어가고 h가 23시일때 23시=>0시





# print(a/4)#몫
# print(a%4)#나머지