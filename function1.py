# function

#함수 정의
def setValue(newValue):
    x = newValue
    print('지역변수:',x)

#호출
retValue = setValue(5)
print(retValue)

#튜플로 리턴
def swap(x,y):
    return y,x

#호출
print(swap(3,4))

#지역변수와 전역변수
def func1(a):
    return a+x

#호출
x = 5
print(func1(1))

def func2(a):
    x = 10
    return a+x

print(func2(1))

#디버깅
#교집합 리턴 함수
def intersect(prelist, postlist):
    result = []
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

#호출
print(intersect('HAAM','SPAM'))

#기본값 세팅
def times(a=10,b=20):
    return a*b

#호출
print(times())
print(times(5))
print(times(5,6))

#키워드 인자
def connectURL(server,port):
    strURL = "https://"+server+":"+port
    return strURL

#호출
print(connectURL('multi.com','80'))
print(connectURL(port='80',server='test.com'))