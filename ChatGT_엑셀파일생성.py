from openpyxl import Workbook
from random import randint

# 제품 정보 생성
def generate_product_data():
    products = []
    for i in range(1, 101):
        product_id = f"PROD{i:03}"
        product_name = f"제품 {i}"
        quantity = randint(1, 10)
        price = randint(1000, 100000)
        products.append((product_id, product_name, quantity, price))
    return products

# 제품 데이터를 Excel 파일로 저장
def save_to_excel(products, filename):
    wb = Workbook()
    ws = wb.active
    ws.append(["제품ID", "제품명", "수량", "가격"])
    for product in products:
        ws.append(product)
    wb.save(filename)

# 제품 데이터 생성
products_data = generate_product_data()

# Excel 파일로 저장
save_to_excel(products_data, "c:\\work\\products.xlsx")
