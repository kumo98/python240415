import re

def check_email(email):
    # 이메일 정규 표현식
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # 이메일 주소와 패턴 비교
    if re.match(pattern, email):
        return True
    else:
        return False

# 이메일 주소 테스트
emails = [
    "test@example.com", 
    "invalid.email",
    "another@example.co.uk",
    "john.doe@example.com",
    "alice_123@example.com",
    "invalid@.com",
    "invalid.email@com",
    "test123@test",
    "user@example.co.kr",
    "email_with.dots@example.com"
]

for email in emails:
    if check_email(email):
        print(f"{email} is a valid email address.")
    else:
        print(f"{email} is not a valid email address.")
