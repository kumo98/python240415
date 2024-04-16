#db1.py

import sqlite3

con = sqlite3.connect(':memory:')

cur = con.cursor()

#테이블 생성
cur.execute('create table PhoneBook(Name text, PhoneNum text);')

#1건 입력
cur.execute('insert into PhoneBook values("홍길동","010-1111-2222");')
cur.execute('insert into PhoneBook values("고길동","010-3333-2222");')

#외부에서 입력 파라미터 처리
name = '전우치'
phoneNum = '010-4444-5555'

cur.execute('insert into PhoneBook values(?,?);',(name,phoneNum))

#검색
cur.execute('select * from PhoneBook;')
for row in cur:
    print(row)