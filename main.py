import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Book, Shop, Stock, Sale, drop_tables, get_shops
import json
from tqdm import tqdm


user = 'postgres'
password = 'введите свой пароль'
host = 'localhost'
base_name = 'book'
DSN = f'postgresql://{user}:{password}@{host}:5432/{base_name}'
engine = sqlalchemy.create_engine(DSN)

# create_tables(engine)
# drop_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

# with open('tests_data.json', 'r') as file:
#     data = json.load(file)
#
# for record in tqdm(data):
#     fields = record.get('fields')
#     # print(type(fields.get('name')))
#     if record.get('model') == 'publisher':
#         # print('publisher')
#         session.add(
#             Publisher(
#                 publisher_id=int(record.get('pk')),
#                 name=fields.get('name')
#             )
#         )
#     elif record.get('model') == 'book':
#         # print('book')
#         session.add(
#             Book(
#                 book_id=record.get('pk'),
#                 title=fields.get('title'),
#                 publisher_id=fields.get('id_publisher')
#             )
#         )
#     elif record.get('model') == 'shop':
#         # print('shop')
#         session.add(
#             Shop(
#                 shop_id=record.get('pk'),
#                 name=fields.get('name')
#             )
#         )
#     elif record.get('model') == 'stock':
#         # print('stock')
#         session.add(
#             Stock(
#                 stock_id=record.get('pk'),
#                 book_id=fields.get('id_book'),
#                 shop_id=fields.get('id_shop'),
#                 count=fields.get('count')
#             )
#         )
#     elif record.get('model') == 'sale':
#         # print('sale')
#         session.add(
#             Sale(
#                 sale_id=record.get('pk'),
#                 price=fields.get('price'),
#                 data_sale=fields.get('date_sale'),
#                 stock_id=fields.get('id_stock'),
#                 count=fields.get('count')
#             )
#         )
# session.commit()


res_2 = get_shops(session, "Pearson")
print(*res_2, sep='\n')

session.close()



