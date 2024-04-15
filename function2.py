#function2

#가변인자 처리
def union(*arg):
    result = []
    for item in arg:
        for x in item:
            if x not in result:
                result.append(x)
    return result

#여러가지 경우
print(union('HAM','SPAM'))
print(union('HAM','SPAM','EGG'))