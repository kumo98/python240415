#db1.py

import sqlite3

# con = sqlite3.connect(':memory:')
con = sqlite3.connect('c:\\work\\sample.db')

cur = con.cursor()

#테이블 생성
cur.execute('create table if not exists PhoneBook(Name text, PhoneNum text);')

#1건 입력
cur.execute('insert into PhoneBook values("홍길동","010-1111-2222");')
cur.execute('insert into PhoneBook values("고길동","010-3333-2222");')

#외부에서 입력 파라미터 처리
name = '전우치'
phoneNum = '010-4444-5555'

cur.execute('insert into PhoneBook values(?,?);',(name,phoneNum))

#다중행을 입력
datalist = (('김길동','010-5555-5555'),('임길동','010-4444-6666'))

cur.executemany('insert into PhoneBook values(?,?);',datalist)

#검색
cur.execute('select * from PhoneBook;')

# for row in cur:
#     print(row)

print(cur.fetchall())

#작업 완료
con.commit()