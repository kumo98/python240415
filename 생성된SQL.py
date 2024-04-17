import sqlite3
import random
import string

class ProductDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS products (
                            id INTEGER PRIMARY KEY,
                            name TEXT,
                            price REAL)''')
        self.conn.commit()

    def insert_product(self, name, price):
        self.cur.execute('''INSERT INTO products (name, price) VALUES (?, ?)''', (name, price))
        self.conn.commit()

    def update_product_price(self, product_id, new_price):
        self.cur.execute('''UPDATE products SET price = ? WHERE id = ?''', (new_price, product_id))
        self.conn.commit()

    def delete_product(self, product_id):
        self.cur.execute('''DELETE FROM products WHERE id = ?''', (product_id,))
        self.conn.commit()

    def select_product(self, product_id):
        self.cur.execute('''SELECT * FROM products WHERE id = ?''', (product_id,))
        return self.cur.fetchone()

def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def generate_sample_data(database, num_entries):
    for _ in range(num_entries):
        name = generate_random_string(8)
        price = random.uniform(10, 1000)
        database.insert_product(name, price)

if __name__ == "__main__":
    db = ProductDatabase('products.db')

    # 샘플 데이터 생성
    generate_sample_data(db, 100)

    # 제품 정보 조회
    product_id = 1
    product_info = db.select_product(product_id)
    print("Selected Product Info:", product_info)

    # 제품 가격 업데이트
    new_price = 500
    db.update_product_price(product_id, new_price)

    # 업데이트된 제품 정보 조회
    updated_product_info = db.select_product(product_id)
    print("Updated Product Info:", updated_product_info)

    # 제품 삭제
    db.delete_product(product_id)

    # 삭제 후 제품 정보 조회
    deleted_product_info = db.select_product(product_id)
    print("Deleted Product Info:", deleted_product_info)
